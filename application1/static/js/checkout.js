// document.addEventListener("DOMContentLoaded", function () {
//     const numPersonsInput = document.getElementById('num-persons');
//     const totalPriceElement = document.getElementById('total-price');
//     const productPrice = parseInt(document.querySelector('.price').textContent.replace('₹', ''));
    
//     numPersonsInput.addEventListener('input', function () {
//         const numPersons = parseInt(this.value) || 1;  // Default to 1 if input is empty or invalid
//         const totalPrice = numPersons * productPrice;
        
//         totalPriceElement.textContent = totalPrice;
//     });
// });
// -----------------------------------------------------------------------------------------------------//
document.addEventListener("DOMContentLoaded", function () {
    const numPersonsInput = document.getElementById('num-persons');
    const totalPriceElement = document.getElementById('total-price');
    const productPrice = parseInt(document.querySelector('.price').textContent.replace('₹', ''));

    numPersonsInput.addEventListener('input', function () {
        const numPersons = parseInt(this.value) || 1;  // Default to 1 if input is empty or invalid
        const totalPrice = numPersons * productPrice;
        
        // Update the total price in the UI
        totalPriceElement.textContent = totalPrice;
    });
});