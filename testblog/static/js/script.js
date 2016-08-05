/**
 * Created by artur on 18.07.2016.
 */
jQuery(document).ready(function($) {

    $("#myTable").tablesorter({

        widgets:['zebra'],
        debug:true,
        widthFixed:false,
        widgetOptions: {
            resizable: true,

            resizable_widths : [ '10%', '10%', '40px', '10%', '100px' ]
        }

    })
        .tablesorterPager({
            size:10,
            container:$('#pager'),
            positionFixed:false,
            page:2,
            cssNext:'.next',
            cssPrev:'.prev',
            cssFirst:'.first',
            cssLast:'.last',
        });

});


$(document).ready(function(){

    $("#name").change(function(){


        var regexp = /^[A-Za-z0-9]{3,30}$/;

        var x=$(this).val();

        if(regexp.test(x)) {

            $(this).css({"border-color": "green",

                "border-style":"solid"});
            $("#send_btn").prop('disabled', false);

        }
        else {


            $(this).css({"border-color": "red",

                "border-style":"solid"});
            $("#send_btn").prop('disabled', true);
        }

    });

});


$(document).ready(function(){

    $("#homepage").change(function(){

        var regexp =  /(([a-z0-9\-\.]+)?[a-z0-9\-]+(!?\.[a-z]{2,4}))/;

        var x=$(this).val();

        if (regexp.test(x)) {

            $(this).css({
                "border-color": "green",

                "border-style": "solid"
            });

        }
        else {

            $(this).css({
                "border-color": "red",

                "border-style": "solid"
            });

        }

    });

});
