 BreakTheInternetPage = function() {
        var e, t = new SocialModule,
            n = $(window).width(),
            a = $(window).height(),
            i = $(".page-wrap"),
            o = (i.length - 1, $(".subheader-wrap")),
            s = function() {
                $.each(o, function(t, n) {
                    $(".toc-wrap ul").append("<li>" + $(n).find("h2").text() + "</li>"), t === o.length - 1 && (e = $(".toc-wrap ul li"))
                })
            },
            r = function(t) {
                $(e).removeClass("active");
                for (var n = 0; n < currSec + 1; n++) $(e[n]).addClass("active")
            },
            c = function() {
                $("body").hasClass("accept-nsfw") && (currSec = $(this).index(), $("html,body").animate({
                    scrollLeft: $(o[currSec]).offset().left - 65
                }, 1250, "easeInOutQuart"), r(), $(".toc-wrap").removeClass("open"), ga("send", "event", "#BreakTheInternet", "click", "Table Of Contents - Item"))
            };
        $(".toc-wrap ul").on("click", "li", c);
        var d = function() {
            var e = 0;
            $.each(i, function(t, n) {
                $(n).css("left", e), e += $(n).width()
            })
        };
        $(".open-story .simple-btn").on("click", function() {
            $("body").addClass("accept-nsfw"), n >= 900 ? $("html,body").animate({
                scrollLeft: $(".story-start").offset().left - 65
            }, 1250, "easeInOutQuart") : $("html,body").animate({
                scrollTop: $(".story-start").offset().top - 65
            }, 1250, "easeInOutQuart")
        });
        var h = function() {
            var e = $(this).parents(".media-wrap").find("iframe").attr("data-src"),
                t = $(this).parent();
            $(this).parents(".media-wrap").find("iframe").attr("src", e), t.animate({
                opacity: 0
            }, 600, function() {
                t.remove()
            })
        };
        $(".media-wrap .play-btn-wrap").on("click", h), $(".social-icons a").on("click", function(e) {
            var n = "http://series.hashtagsunplugged.com/BreakTheInternet",
                a = "The Story Behind #BreakTheInternet which which exploded Kim Kardashian's naked photoshoot on the cover of Paper magazine. #BehindTheHashtag",
                i = $(this).attr("data-social");
            t.share(e, i, n, a)
        }), $("body").on("mousewheel", function(e, t) {
            $("body").hasClass("accept-nsfw") && (e.preventDefault(), this.scrollLeft -= 2 * t)
        }), $(window).on("resize", function() {
            n = $(window).width(), a = $(window).height(), d()
        }), $(window).on("load", function() {
            d(), $(window).scrollLeft(0), $(window).scrollTop(0)
        }), $(document).on("ready", function() {
            s(), d(), setTimeout(function() {
                $(window).scrollLeft(0), $(window).scrollTop(0)
            }, 100), $(".social-icons a.email").attr("href", "mailto:?subject=" + encodeURIComponent("Check Out The Story Behind #BreakTheInternet") + "&body=" + encodeURIComponent("Paper Magazine set out with the deliberate intention of breaking the internet with the cover of their Winter 2014 issue. It featured a photo of Kim Kardashian balancing a champagne glass on her rear-end and a simple, bold headline: Break The Internet / Kim Kardashian. This image was released online on November 11, 2014. \n\n* This story is NSFW. \n\nRead the story behind #BreakTheInternet here: series.hashtagsunplugged.com/breaktheinternet"))
        })