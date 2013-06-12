(function($) {
    $(document).ready(function () {
        $('#changelist-filter ul, #changelist-filter h3, #hideFilter').hide();
        $('#changelist-filter h2').css('cursor', 'pointer');
        $('#changelist-filter h2').click(function () {
            if ($('#changelist-filter ul:visible').length > 0) {
                $('#changelist-filter ul, #changelist-filter h3').hide();
                $('#hideFilter').hide();
                $('#showFilter').show();
            } else {
                $('#changelist-filter ul, #changelist-filter h3').show();
                $('#hideFilter').show();
                $('#showFilter').hide();
            }
        });
    });
})(django.jQuery);
