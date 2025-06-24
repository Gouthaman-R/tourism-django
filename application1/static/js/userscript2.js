
// // <---------------menubar--------------------->

// const menuIcon = document.getElementById('menu-icon');
// const menuBar = document.getElementById('menu-bar');

// // Toggle menu visibility on menu icon click
// menuIcon.addEventListener('click', function() {
//     // Toggle the display of the menu bar
//     if (menuBar.style.display === 'block') {
//         menuBar.style.display = 'none';
//     } else {
//         menuBar.style.display = 'block';
//     }
// });

// // Hide the menu bar when the cursor leaves it
// menuBar.addEventListener('mouseleave', function() {
//     menuBar.style.display = 'none';
// });




document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const menuBar = document.querySelector(".menu-bar");

    // Toggle menu on icon click
    menuIcon.addEventListener("click", () => {
        menuBar.classList.toggle("active");
    });

    // Hide menu when mouse leaves the menu area
    menuBar.addEventListener("mouseleave", () => {
        menuBar.classList.remove("active");
    });
});



// <-------------------product carousel---------------------->

document.querySelectorAll('.carousel').forEach((carousel) => {
    let currentSlide = 0;
    const images = carousel.querySelectorAll('.product-image'); // Select images within this carousel
    let slideInterval = setInterval(nextSlide, 3000); // Change image every 3 seconds

    function showSlide(index) {
        images.forEach((img, i) => {
            img.classList.remove('active');
            if (i === index) img.classList.add('active');
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % images.length;
        showSlide(currentSlide);
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + images.length) % images.length;
        showSlide(currentSlide);
    }

    // Reset interval when user navigates manually
    function resetInterval() {
        clearInterval(slideInterval);
        slideInterval = setInterval(nextSlide, 3000);
    }

    // Attach resetInterval to buttons within the current carousel
    carousel.querySelector('.next').addEventListener('click', () => {
        nextSlide();
        resetInterval();
    });

    carousel.querySelector('.prev').addEventListener('click', () => {
        prevSlide();
        resetInterval();
    });

    // Initialize the first slide as active
    showSlide(currentSlide);
});






// --------------------------------------------------------------------------------//


// document.querySelectorAll('.favorite-btn').forEach(button => {
//     button.addEventListener('click', function() {
//         const productId = this.getAttribute('data-product-id');
//         const url = `/add-to-favorites/${productId}/`;
        
//         fetch(url, {
//             method: 'GET',  // or 'POST' depending on your implementation
//             headers: {
//                 'X-CSRFToken': '{{ csrf_token }}',  // Important for CSRF protection
//             },
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 // Update the button text based on whether it was added or removed
//                 if (this.innerText.includes('Add')) {
//                     this.innerText = '❤️ Remove from Favorites';
//                 } else {
//                     this.innerText = '♡ Add to Favorites';
//                 }
//             } else {
//                 alert(data.message);  // Display error message
//             }
//         });
//     });
// });


// <----------------------my favorites--------------------------->//

document.querySelectorAll('.favorite-btn').forEach(button => {
    button.addEventListener('click', function() {
        const productId = this.getAttribute('data-product-id');
        const url = `/add-to-favorites/${productId}/`;
        
        fetch(url, {
            method: 'GET',  // or 'POST' depending on your implementation
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',  // Important for CSRF protection
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Update the button icon based on whether it was added or removed
                if (this.innerText.includes('♡')) {
                    this.innerText = '❤️';  // Change to filled heart if just added
                    this.style.fontSize = '19px';

                } else {
                    this.innerText = '♡';  // Change to empty heart if just removed
                    this.style.fontSize = '28px';
                }
                
            } else {
                alert(data.message);  // Display error message
            }
        });
    });
});


// <---------------------------add to cart---------------------------------->//
document.querySelectorAll('.cart-btn').forEach(button => {
    button.addEventListener('click', function() {
        const productId = this.getAttribute('data-product-id');
        const url = `/add-to-cart/${productId}/`;

        fetch(url, {
            method: 'GET',  // You can use POST if preferred
            headers: {
                'X-CSRFToken': '{{ csrf_token }}',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Change the button text or style if needed
                alert(data.message);  // For now, just show an alert
            } else {
                alert(data.message);
            }
        });
    });
});
// 


// ----------------------------------search Bar--------------------------------------//


// document.getElementById('search-input').addEventListener('input', function() {
//     const query = this.value;
//     if (query.length > 2) {
//         fetch(`/search/?query=${query}`)
//             .then(response => response.json())
//             .then(products => {
//                 const resultsContainer = document.getElementById('search-results');
//                 resultsContainer.innerHTML = ''; // Clear previous results
//                 products.forEach(product => {
//                     const resultItem = document.createElement('div');
//                     resultItem.className = 'search-result';
//                     resultItem.textContent = product.title;
//                     resultItem.onclick = function() {
//                         window.location.href = `/product/${product.id}/`; // Redirect to product page
//                     };
//                     resultsContainer.appendChild(resultItem);
//                 });
//             });
//     } else {
//         document.getElementById('search-results').innerHTML = ''; // Clear if query is too short
//     }
// });


document.getElementById('search-input').addEventListener('input', function() {
    const query = this.value;
    if (query.length > 2) {
        fetch(`/search/?query=${query}`)
            .then(response => response.json())
            .then(products => {
                const resultsContainer = document.getElementById('search-results');
                resultsContainer.innerHTML = ''; // Clear previous results
                products.forEach(product => {
                    const resultItem = document.createElement('div');
                    resultItem.className = 'search-result';
                    resultItem.textContent = product.title;
                    resultItem.onclick = function() {
                        window.location.href = `/product/${product.id}/`; // Redirect to product page
                    };
                    resultsContainer.appendChild(resultItem);
                });
            });
    } else {
        document.getElementById('search-results').innerHTML = ''; // Clear if query is too short
    }
});



// ---------------------------------userpage carousel---------------------------------//
let currentIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;
let autoSlideInterval;

function showSlide(index) {
    const track = document.getElementById('track');
    track.style.transform = `translateX(-${index * 100}%)`;
}

function moveSlide(step) {
    currentIndex = (currentIndex + step + totalSlides) % totalSlides;
    showSlide(currentIndex);
    resetAutoSlide();
}

function startAutoSlide() {
    autoSlideInterval = setInterval(() => {
        currentIndex = (currentIndex + 1) % totalSlides;
        showSlide(currentIndex);
    }, 3000); // Adjust time interval as needed
}

function resetAutoSlide() {
    clearInterval(autoSlideInterval);
    startAutoSlide();
}

// Start auto-sliding on page load
window.onload = startAutoSlide;



// -------------------------chat-BOT-----------------------------//


async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    
    // Get the CSRF token from the page
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch('/chatbot/get-response/', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: `message=${userInput}`,  // Send the user input as a POST body
    });
    
    const data = await response.json();
    
    // Update the chat output with the bot's response
    document.getElementById('chat-output').innerHTML += `<p><strong>You:</strong> ${userInput}</p><p><strong>Bot:</strong> ${data.response}</p>`;
    document.getElementById('user-input').value = '';  // Clear the input after sending
}
        