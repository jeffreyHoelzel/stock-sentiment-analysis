const getStockInsight = async (data, resultsContainer) => {
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
    resultsContainer.insertAdjacentHTML("afterbegin", newContent);
  } catch (error) {
    const newError = `
      <div class="results-container">
        <p class="error-message">${error.message}.</p>
      </div>
    `;
    resultsContainer.insertAdjacentHTML("afterbegin", newError);
    console.log(`Error occured while fetching data: ${error}`);
  }
}

export default getStockInsight;