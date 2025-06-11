let counter = 2;

$(document).ready(function () {
    $("#addInput").click(function () {
        $('#inputs').append(
            `<input type="text" name="input${counter}" placeholder="Имя" class="dynamic-input" style="margin-bottom: 10px">`
        );
        counter++;
    });
});


$(document).ready(function () {
    $("#removeInput").click(
        function () {
            let dynamicInputs = $("#inputs .dynamic-input");

            if (dynamicInputs.length > 1) {
                dynamicInputs.last().remove();
                counter--;
            }
        }
    );
});