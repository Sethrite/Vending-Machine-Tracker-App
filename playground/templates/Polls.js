// Get the vending machine ID from Django context
const machineId = {{ machine.id }};

// Function to fetch updated snack data from the server
function fetchUpdatedData() {
    fetch(`/User/vending-machine/${machineId}/`)
        .then(response => response.json())
        .then(data => {
            data.forEach(snack => {
                // Update each snack's amount in the vending machine
                const snackElement = document.getElementById(`snack-${snack.id}`);
                if (snackElement) {
                    snackElement.querySelector('.amount').innerText = `Amount: ${snack.amount}`;
                }
            });
        })
        .catch(error => console.error('Error fetching data:', error));
}

// Fetch data every second
setInterval(fetchUpdatedData, 1000);