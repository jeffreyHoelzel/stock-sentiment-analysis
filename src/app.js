import getStockInsight from "./components/StockInsight.js";

document.addEventListener("DOMContentLoaded", () => {
  // get html elements for data retrieval, transfer, and formatting on page
  const tickerSymbolInput = document.getElementById("ticker-symbol-input");
  const fromDateInput = document.getElementById("from-date-input");
  const toDateInput = document.getElementById("to-date-input");
  const formBody = document.getElementById("form-body");
  const submitButton = document.getElementById("submit-data");
  const results = document.getElementById("results");

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

    getStockInsight(stockQueryParams, results);
    formBody.reset();
  });

  // attempt tp prevent form from automatically submitting
  formBody.addEventListener("submit", (e) => {
    e.preventDefault();
  });
});