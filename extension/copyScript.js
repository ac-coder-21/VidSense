document.addEventListener('DOMContentLoaded', function () {
    const outputParagraph = document.getElementById('output');
    const copyIcon = document.getElementById('copy-icon');

    copyIcon.addEventListener('click', function () {
        const textToCopy = outputParagraph.textContent;
        const tempTextArea = document.createElement('textarea');
        tempTextArea.value = textToCopy;
        document.body.appendChild(tempTextArea);
        tempTextArea.select();
        document.execCommand('copy');
        document.body.removeChild(tempTextArea);
        alert('Text copied to clipboard!');
    });
});
