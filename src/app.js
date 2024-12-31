document.addEventListener("DOMContentLoaded", () => {
  // get html elements for data retrieval, transfer, and formatting on page
  const tickerSymbolInput = document.getElementById("ticker-symbol-input");
  const fromDateInput = document.getElementById("from-date-input");
  const toDateInput = document.getElementById("to-date-input");
  const formBody = document.getElementById("form-body");
  const submitButton = document.getElementById("submit-data");
  const results = document.getElementById("results");

  // function to fetch response from backend giving stock insight
  const getStockInsight = async (data) => {
    try {
      const response = await fetch(`http://localhost:5000/get-insight?${data}`, {
        method: "GET"
      });

      if (!response.ok) {
        throw new Error(`Server responsed with status code: ${response.status}`)
      }

      // if status is 200 (ok), get data in json format
      const stockInsightData = await response.json();

      // display data to user
      const newContent = `
        <div class="results-container">
          <h2 class="ticker-header">${stockInsightData.ticker}</h2>
          <p class="dates"><strong>From:</strong> ${stockInsightData.fromDate}, <strong>To:</strong> ${stockInsightData.toDate}</p>
          <p class="summary"><strong>Summary:</strong> ${stockInsightData.summary}</p>
        </div>
      `;
      results.insertAdjacentHTML("afterbegin", newContent);
    } catch (error) {
      const newError = `
        <div class="results-container">
          <p class="error-message">${error.message}.</p>
        </div>
      `;
      results.insertAdjacentHTML("afterbegin", newError);
      console.log(`Error occured while fetching data: ${error}`);
    }
  }

  // listen for form button clicks
  submitButton.addEventListener("click", (e) => {
    e.preventDefault();

    // set up stock object and encode as url search param
    const stockQueryData = {
      ticker: tickerSymbolInput.value.toUpperCase(), 
      fromDate: fromDateInput.value, 
      toDate: toDateInput.value
    };
    const stockQueryParams = new URLSearchParams(stockQueryData).toString();

    getStockInsight(stockQueryParams);
    formBody.reset();
  });

  // attempt tp prevent form from automatically submitting
  formBody.addEventListener("submit", (e) => {
    e.preventDefault();
  });
});