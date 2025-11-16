// Notification System
function showNotification(message, type = 'info') {
    let container = document.getElementById('notification-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'notification-container';
        container.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 9999;
            max-width: 400px;
        `;
        document.body.appendChild(container);
    }
    
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <span>${message}</span>
        <button onclick="closeNotification(this)" style="background: none; border: none; color: white; font-size: 18px; cursor: pointer; padding: 0; margin-left: 15px; width: 20px; height: 20px;">&times;</button>
    `;
    
    // Set notification styles
    const styles = {
        'info': 'background: linear-gradient(135deg, #3498db, #2980b9);',
        'warning': 'background: linear-gradient(135deg, #f39c12, #e67e22);',
        'error': 'background: linear-gradient(135deg, #e74c3c, #c0392b);',
        'success': 'background: linear-gradient(135deg, #27ae60, #229954);'
    };
    
    notification.style.cssText = `
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 15px 20px;
        margin-bottom: 10px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        animation: slideIn 0.3s ease-out;
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        line-height: 1.4;
        color: white;
        ${styles[type] || styles.info}
    `;
    
    container.appendChild(notification);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        if (notification.parentNode) {
            closeNotification(notification.querySelector('button'));
        }
    }, 5000);
}

function closeNotification(button) {
    const notification = button.parentNode;
    notification.style.animation = 'slideOut 0.3s ease-in-out';
    setTimeout(() => {
        if (notification.parentNode) {
            notification.parentNode.removeChild(notification);
        }
    }, 300);
}

// Check cart before checkout
function checkCartBeforeCheckout() {
    fetch('/cart/', {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.text())
    .then(html => {
        // Simple check if cart is empty by looking for the empty message
        if (html.includes('Your cart is empty') || html.includes('No items in your cart')) {
            showNotification('Your cart is empty. Please add some items before checkout.', 'warning');
        } else {
            // Cart has items, proceed to checkout
            window.location.href = '/checkout/';
        }
    })
    .catch(error => {
        console.error('Error checking cart:', error);
        showNotification('Unable to check cart. Please try again.', 'error');
    });
}

// Logout confirmation
function confirmLogout() {
    document.getElementById('logoutModal').style.display = 'block';
}

// Generic modal close function
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Original carousel code
document.addEventListener('DOMContentLoaded', () => {
    const carousel = document.getElementById('productsCarousel');
    const prevBtn = document.getElementById('productsPrev');
    const nextBtn = document.getElementById('productsNext');

    if (!carousel || !prevBtn || !nextBtn) return;

    const scrollAmount = 260;

    prevBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });

    nextBtn.addEventListener('click', () => {
        carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });
});
