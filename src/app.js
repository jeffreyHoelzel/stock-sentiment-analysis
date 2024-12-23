document.addEventListener("DOMContentLoaded", () => {
  // html elements to use
  const header1 = document.getElementById("header1");
  const button1 = document.getElementById("button1");

  const renderPage = async () => {
    try {
      const response = await fetch("http://localhost:5000/get", {
        method: "GET", 
        headers: {
          "Content-Type": "application/json"
        }
      });

      if (!response.ok) {
        throw new Error(`Server responsed with status: ${response.status}`);
      }

      const data = await response.json();
      header1.innerHTML += `${data.text}`;
    } catch (error) {
      console.log("Error during fetch:", error);
    }
  }

  button1.addEventListener("click", (e) => {
    e.preventDefault();

    renderPage();
  });
});