

function trace_djevents(element) {
    element.on('djselectablecreate', function(event) { console.log('djselectablecreate: %o', event.target); });
    element.on('djselectablesearch', function(event) { console.log('djselectablesearch: %o', event.target); });
    element.on('djselectableopen', function(event) { console.log('djselectableopen: %o', event.target); });
    element.on('djselectablefocus', function(event) { console.log('djselectablefocus: %o', event.target); });
    element.on('djselectableselect', function(event) { console.log('djselectableselect: %o', event.target); });
    element.on('djselectableclose', function(event) { console.log('djselectableclose: %o', event.target); });
    element.on('djselectablechange', function(event) { console.log('djselectablechange: %o', event.target); });
}



$(document).ready(function() {

    if ($('body').hasClass('add-form')) {
    }

    if ($('body').hasClass('change-form')) {

        $(document).ready(function() {

            //trace_djevents($('#id_city'));
            trace_djevents($('#id_city_0'));

            $('#id_country').on('change', function(event) {
                $('#id_city_0').val(null);
                $('#id_city_1').val(null);
            });

            $('#id_city_0').djselectable('option', 'prepareQuery', function(query) {
                query.country_id = $('#id_country').val();
            });

        });

    }

});
