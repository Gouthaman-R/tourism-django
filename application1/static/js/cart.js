// <------------------------------------person count-total--------------------->


document.addEventListener("DOMContentLoaded", function () {
    // Loop through all number of persons input fields
    document.querySelectorAll('.num-persons').forEach(input => {
        input.addEventListener('input', function () {
            const productId = this.getAttribute('data-product-id');
            const numPersons = parseInt(this.value) || 1; // Default to 1 if input is empty
            const productPrice = parseInt(document.querySelector(`#price-${productId}`).textContent.replace('₹', ''));
            const totalPrice = numPersons * productPrice;

            console.log(`Product ID: ${productId}, Number of Persons: ${numPersons}, Product Price: ₹${productPrice}, Total Price: ₹${totalPrice}`);
            console.log('hello')
            // Update the total price for this product
            const totalPriceElement = document.querySelector(`#total-price-${productId}`);
            totalPriceElement.textContent = totalPrice;
        });
    });
});
// -----------------------------------------------------------------------------//
document.addEventListener("DOMContentLoaded", function () {
    const numPersonsInput = document.getElementById('num-persons');
    const totalPriceElement = document.getElementById('total-price');
    const productPrice = parseInt(document.querySelector('.price').textContent.replace('₹', ''));
    
    numPersonsInput.addEventListener('input', function () {
        const numPersons = parseInt(this.value) || 1;  // Default to 1 if input is empty or invalid
        const totalPrice = numPersons * productPrice;
        
        totalPriceElement.textContent = totalPrice;
    });
});


