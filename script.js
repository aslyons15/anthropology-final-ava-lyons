$(document).ready(function(){
            // Activate carousel
            $("#myCarousel").carousel();
            // Enable carousel control
            $(".carousel-control-prev").click(function(){
                $("#myCarousel").carousel('prev');
            });
            $(".carousel-control-next").click(function(){
                $("#myCarousel").carousel('next');
            });
            // Enable carousel indicators
            $(".slide-one").click(function(){
                $("#myCarousel").carousel(0);
            });
            $(".slide-two").click(function(){
                $("#myCarousel").carousel(1);
            });
            $(".slide-three").click(function(){
                $("#myCarousel").carousel(2);
            });
        });