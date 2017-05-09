window.scrollHandler = function () {
    function once(fn) {
        var called = false;
        return function (a) {
            if (!called)
                fn(a);
            called = true
        }
    }
//NAVBAR TRACKING
    $('section').scrollfire({

        // Offsets
        offset: 0,
        topOffset: 500,
        bottomOffset: 500,

        onTopIn: activateSection,
        onBottomIn: activateSection,
    });

    function activateSection(elm,a,b) {
        console.log(elm,a,b);
        var hash = '#' + elm.id;
        $('ul.navbar-nav li a').removeClass('active');
        $('ul.navbar-nav li a[href="' + hash + '"]').addClass('active')
    }

    $('.section-wrapper').scrollfire({

        // Offsets
        offset: 0,
        topOffset: 300,
        bottomOffset: 250,

        onBottomIn: loadSection
    });

    function loadSection(elm) {
        $(elm).find('section').addClass('loaded')
    }

//TRANSFORM LOADING
    $('.counter-row').scrollfire({

        // Offsets
        offset: 0,
        topOffset: 300,
        bottomOffset: 250,

        onBottomIn: once(numbers)
    });
    function numbers() {
        $('.counter-row b').each(function (idx, element) {
            var $elem = $(element);
            var count = parseInt($elem.text());
            $elem.animateNumber(
                {
                    number: count,
                    // 'font-size': '50px',
                    'opacity': '1',
                    easing: 'easeInQuad', // require jquery.easing
                },
                Math.min(count * 2 + 600, 1000)
            );
        });

    }
}