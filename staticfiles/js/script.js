
function toggleAmountInput(event) {
    var otherInput = document.querySelector('.amount-input');
    if (event.target.id === 'other' && event.target.checked) {
        otherInput.classList.add('active');
        otherInput.setAttribute('required', 'required');
    } else {
        otherInput.classList.remove('active');
        otherInput.removeAttribute('required');
        otherInput.value = '';
    }
    updateAmountWithPercent();
}

function updateAmountWithPercent() {
    var selectedAmount = document.querySelector('.btn-radio:checked').parentNode.nextElementSibling.querySelector('h4').innerText;
    selectedAmount = parseFloat(selectedAmount.replace('$', '').replace(',', ''));
    var addPercent = selectedAmount * 0.025;
    var totalAmount = selectedAmount + addPercent;
    document.getElementById('total-amount').innerText = '$' + totalAmount.toFixed(2);
}

function validateAmountInput(event) {
    if (event.target.value < 1) {
        event.target.value = '';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var radioButtons = document.querySelectorAll('input[name="amount"]');
    radioButtons.forEach(function(radio) {
        radio.addEventListener('change', toggleAmountInput);
    });

    var otherAmountInput = document.querySelector('.amount-input');
    otherAmountInput.addEventListener('input', function() {
        validateAmountInput(event);
        updateAmountWithPercent();
    });
});
function toggleAmountInput(event) {
    const otherAmountInput = document.getElementById('other-amount');
    if (event.target.checked) {
        otherAmountInput.style.display = 'block';
    } else {
        otherAmountInput.style.display = 'none';
    }
}