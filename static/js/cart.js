document.addEventListener('DOMContentLoaded', () => {
    const cartRows = document.querySelectorAll('.cart-row');
    const cartTotalEl = document.querySelector('#cart-total');

    function recalcCartTotal() {
        let total = 0;
        document.querySelectorAll('.line-total').forEach(line => {
            const value = parseFloat(line.dataset.value || 0);
            total += value;
        });
        cartTotalEl.textContent = '₱' + total.toFixed(2);
    }

    cartRows.forEach(row => {
        const price = parseFloat(row.dataset.price);
        const qtyInput = row.querySelector('.item-qty');
        const minusBtn = row.querySelector('.qty-btn.minus');
        const plusBtn = row.querySelector('.qty-btn.plus');
        const lineTotalEl = row.querySelector('.line-total');

        function updateLine() {
            let qty = parseInt(qtyInput.value) || 1;
            if (qty < 1) qty = 1;
            qtyInput.value = qty;

            const lineTotal = price * qty;
            lineTotalEl.textContent = '₱' + lineTotal.toFixed(2);
            lineTotalEl.dataset.value = lineTotal.toString();

            recalcCartTotal();
        }

        minusBtn.addEventListener('click', () => {
            qtyInput.value = Math.max(1, (parseInt(qtyInput.value) || 1) - 1);
            updateLine();
        });

        plusBtn.addEventListener('click', () => {
            qtyInput.value = (parseInt(qtyInput.value) || 1) + 1;
            updateLine();
        });

        qtyInput.addEventListener('change', updateLine);

        // initial calc
        updateLine();
    });
});