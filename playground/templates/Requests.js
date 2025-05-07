const machineId = {{ machine.id }};  // Get the vending machine ID from Django context

    function fetchUpdatedData() {
        fetch(`/Manufacturer/vending-machine/${machineId}/`)
            .then(response => response.json())
            .then(data => {
                data.forEach(snack => {
                    const snackElement = document.getElementById(`snack-${snack.id}`);
                    if (snackElement) {
                        snackElement.querySelector('.amount').innerText = `Amount: ${snack.amount}`;
                    }
                });
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    function handleRestock(event) { 
    const snackId = event.target.getAttribute('data-id'); // Get snack_id from the button's data attribute
    console.log('Restocking snack with ID:', snackId); // Debugging output

    fetch(`/Manufacturer/vending-machine/${machineId}/restock/?snack_id=${snackId}`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const snackElement = document.getElementById(`snack-${snackId}`);
                if (snackElement) {
                    snackElement.querySelector('.amount').innerText = `Amount: 10`; // Update amount displayed on UI
                }
                console.log(data.message); // Log success message
            } else {
                console.error('Error:', data.message); // Log error message
            }
        })
        .catch(error => console.error('Error restocking:', error));
    }

    function handleResetAll() {
        if (confirm('Are you sure you want to reset all items to 10?')) {
            fetch(`/Manufacturer/vending-machine/reset/`)
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert(data.message);
                    fetchUpdatedData(); // Fetch updated data to reflect changes
                } else {
                    console.error('Error:', data.message);
                }
            })
            .catch(error => console.error('Error resetting snacks:', error));
        }
    }

    document.querySelectorAll('.restock-button').forEach(button => {
        button.addEventListener('click', handleRestock);
    });

    document.addEventListener('scroll', function() {
        const button = document.getElementById('reset-all-button');
        const footer = document.querySelector('footer');
        const footerRect = footer.getBoundingClientRect(); // Get footer position
        const buttonRect = button.getBoundingClientRect(); // Get button position
        const offset = 50; // Distance before footer to stop the button

        // Check if the button is too close to the footer
        if (footerRect.top <= window.innerHeight - buttonRect.height - offset) {
            button.style.bottom = `${footerRect.height + offset}px`; // Position the button just above the footer
        } else {
            button.style.bottom = '100px'; // Reset to original position when there's enough space
        }
    });

    // Fetch data every second to keep quantities updated
    setInterval(fetchUpdatedData, 1000);