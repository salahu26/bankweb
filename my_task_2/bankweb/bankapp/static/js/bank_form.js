document.addEventListener('DOMContentLoaded', function() {
    var districtSelect = document.getElementById('id_district');
    var branchSelect = document.getElementById('id_branch');

    // Define the branch choices for each district
    var branchChoices = {
        'Alappuzha': [('Aroor', 'Aroor'), ('Kayamkulam', 'AKayamkulamluva')],
            'Ernakulam': [('edappaly', 'Edappaly'), ('Aluva', 'Aluva')],
            'Idukki': [('Thodupuzha', 'Thodupuzha'), ('Kattappana', 'Kattappana')],
            'Kannur': [('Thalassery', 'Thalassery'), ('Payangadi', 'Payangadi')],
            'Kasaragod': [('Hosdurga', 'Hosdurga'), ('hosabettu', 'hosabettu')],
        // Add choices for other districts as needed
    };

    // Update the branch choices when the district selection changes
    districtSelect.addEventListener('change', function() {
        var selectedDistrict = districtSelect.value;
        var selectedBranchChoices = branchChoices[selectedDistrict] || [];

        // Clear existing options
        branchSelect.innerHTML = '';

        // Add new options
        selectedBranchChoices.forEach(function(branch) {
            var option = document.createElement('option');
            option.value = branch;
            option.text = branch;
            branchSelect.appendChild(option);
        });
    });

    // Trigger a change event to initialize branch choices based on the default district value
    districtSelect.dispatchEvent(new Event('change'));
});
