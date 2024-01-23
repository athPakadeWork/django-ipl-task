const ctx = document.getElementById("myChart");

fetch("http://localhost:8000/schools/dataPerDistrict/")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Failed to fetch data from the server.");
    }
    return response.json();
  })
  .then((data) => {
    console.log(data.data.countOfSchools);
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: data.data.districts,
        datasets: [
          {
            label: "Number of Schools",
            data: data.data.countOfSchools,
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  })
  .catch((error) => {
    console.error("Error:", error.message);
    document.getElementById("errorMessage").innerText =
      "Error: " + error.message;
  });
