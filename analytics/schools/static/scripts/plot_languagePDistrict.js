const ctx = document.getElementById("myChart");
const autocolors = window["chartjs-plugin-autocolors"];

fetch("http://localhost:8000/schools/dataPerLanguage/")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Failed to fetch data from the server.");
    }
    return response.json();
  })
  .then((response) => {
    response = response.data;

    const DATA_COUNT = response.districts.length;
    const NUMBER_CFG = { count: DATA_COUNT, min: 0 };

    const labels = response.districts;
    const datasets = [];
    for (const key in response.languageCount) {
      datasets.push({
        label: key,
        data: response.languageCount[key],
      });
    }

    const data = {
      labels: labels,
      datasets: datasets,
    };
    const config = {
      type: "bar",
      data: data,
      options: {
        responsive: true,
        scales: {
          x: {
            stacked: true,
          },
          y: {
            stacked: true,
          },
        },
      },
    };

    const myChart = new Chart(ctx, config);
  })
  .catch((error) => {
    console.error("Error:", error.message);
    // Display an error message to the user, e.g., append it to the HTML or show a modal

    console.error("Error:", error.message);
    document.getElementById("errorMessage").innerText =
      "Error: " + error.message;
  });
