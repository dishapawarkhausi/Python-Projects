document.addEventListener("DOMContentLoaded", function () {
    const unitCategories = {
        "Length": ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"],
        "Weight": ["kilograms", "grams", "pounds", "ounces"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    };

    const categorySelect = document.getElementById("category");
    const fromUnitSelect = document.getElementById("from_unit");
    const toUnitSelect = document.getElementById("to_unit");

    function populateUnits() {
        const selectedCategory = categorySelect.value;
        fromUnitSelect.innerHTML = "";
        toUnitSelect.innerHTML = "";
        unitCategories[selectedCategory].forEach(unit => {
            let option1 = new Option(unit, unit);
            let option2 = new Option(unit, unit);
            fromUnitSelect.add(option1);
            toUnitSelect.add(option2);
        });
    }

    categorySelect.addEventListener("change", populateUnits);
    populateUnits();

    window.convert = function () {
        const category = categorySelect.value;
        const fromUnit = fromUnitSelect.value;
        const toUnit = toUnitSelect.value;
        const value = document.getElementById("value").value;

        if (!value) {
            alert("Please enter a value to convert.");
            return;
        }

        fetch("/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ category, from_unit: fromUnit, to_unit: toUnit, value })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").textContent = data.result;
        })
        .catch(error => console.error("Error:", error));
    };
});
