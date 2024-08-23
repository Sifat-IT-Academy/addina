(function ($) {
	("use strict");
	var windowOn = $(window);

	/*======================================
	Preloader activation
	========================================*/
	$(window).on("load", function (event) {
		$("#preloader").delay(500).fadeOut(500);
	});

	/*======================================
	Mobile Menu Js
	========================================*/
	$("#mobile-menu").meanmenu({
		meanMenuContainer: ".mobile-menu",
		meanScreenWidth: "991",
		meanExpand: ['<i class="fal fa-plus"></i>'],
	});

	$("#mobile-menu-2").meanmenu({
		meanMenuContainer: ".mobile-menu-2",
		meanScreenWidth: "4000",
		meanExpand: ['<i class="fal fa-plus"></i>'],
	});

	/*======================================
	Sidebar Toggle
	========================================*/
	$(".offcanvas__close,.offcanvas__overlay").on("click", function () {
		$(".offcanvas__info").removeClass("info-open");
		$(".offcanvas__overlay").removeClass("overlay-open");
	});
	$(".sidebar__toggle").on("click", function () {
		$(".offcanvas__info").addClass("info-open");
		$(".offcanvas__overlay").addClass("overlay-open");
	});

	/*======================================
	Body overlay Js
	========================================*/
	$(".body-overlay").on("click", function () {
		$(".offcanvas__area").removeClass("offcanvas-opened");
		$(".df-search-area").removeClass("opened");
		$(".body-overlay").removeClass("opened");
	});

	/*======================================
	Search Header Js
	========================================*/
	$(".search-toggle-open").on("click", function () {
		$(".df-search-area").addClass("opened");
		$(".body-overlay").addClass("opened");
	});
	$(".tp-search-close-btn").on("click", function () {
		$(".df-search-area").removeClass("opened");
		$(".body-overlay").removeClass("opened");
	});

	/*======================================
	Sticky Header Js
	========================================*/

	$(window).scroll(function () {
		if ($(this).scrollTop() > 250) {
			$("#header-sticky").addClass("sticky");
		} else {
			$("#header-sticky").removeClass("sticky");
		}
	});

	/*======================================
	Data Css js
	========================================*/
	$("[data-background").each(function () {
		$(this).css(
			"background-image",
			"url( " + $(this).attr("data-background") + "  )"
		);
	});

	$("[data-width]").each(function () {
		$(this).css("width", $(this).attr("data-width"));
	});

	$("[data-bg-color]").each(function () {
		$(this).css("background-color", $(this).attr("data-bg-color"));
	});

	/*======================================
	 Cart Quantity Js
	========================================*/
	$(".cart-minus").click(function () {
		var $input = $(this).parent().find("input");
		var count = parseInt($input.val()) - 1;
		count = count < 1 ? 1 : count;
		$input.val(count);
		$input.change();
		return false;
	});

	$(".cart-plus").click(function () {
		var $input = $(this).parent().find("input");
		$input.val(parseInt($input.val()) + 1);
		$input.change();
		return false;
	});

	/*======================================
	MagnificPopup image view
	========================================*/
	$(".popup-image").magnificPopup({
		type: "image",
		gallery: {
			enabled: true,
		},
	});

	/*======================================
	MagnificPopup video view
	========================================*/
	$(".popup-video").magnificPopup({
		type: "iframe",
	});

	/*======================================
	Counter Js
	========================================*/
	$(".counter").counterUp({
		delay: 10,
		time: 1000,
	});

	/*======================================
	Wow Js
	========================================*/
	new WOW().init();

	/*======================================
	Back To Top Js
	========================================*/
	var progressPath = document.querySelector(".backtotop-wrap path");
	var pathLength = progressPath.getTotalLength();
	progressPath.style.transition = progressPath.style.WebkitTransition = "none";
	progressPath.style.strokeDasharray = pathLength + " " + pathLength;
	progressPath.style.strokeDashoffset = pathLength;
	progressPath.getBoundingClientRect();
	progressPath.style.transition = progressPath.style.WebkitTransition =
		"stroke-dashoffset 10ms linear";
	var updateProgress = function () {
		var scroll = $(window).scrollTop();
		var height = $(document).height() - $(window).height();
		var progress = pathLength - (scroll * pathLength) / height;
		progressPath.style.strokeDashoffset = progress;
	};
	updateProgress();
	$(window).scroll(updateProgress);
	var offset = 150;
	var duration = 550;
	jQuery(window).on("scroll", function () {
		if (jQuery(this).scrollTop() > offset) {
			jQuery(".backtotop-wrap").addClass("active-progress");
		} else {
			jQuery(".backtotop-wrap").removeClass("active-progress");
		}
	});
	jQuery(".backtotop-wrap").on("click", function (event) {
		event.preventDefault();
		jQuery("html, body").animate({ scrollTop: 0 }, duration);
		return false;
	});

	/*======================================
	For language Js
	========================================*/
	if ($("#header-lang-toggle").length > 0) {
		window.addEventListener("click", function (e) {
			if (document.getElementById("header-lang-toggle").contains(e.target)) {
				$(".header-lang ul").toggleClass("lang-list-open");
			} else {
				$(".header-lang ul").removeClass("lang-list-open");
			}
		});
	}

	/*======================================
	For header header Js
	========================================*/
	if ($("#header-currency-toggle").length > 0) {
		window.addEventListener("click", function (e) {
			if (
				document.getElementById("header-currency-toggle").contains(e.target)
			) {
				$(".tp-header-currency ul").toggleClass("tp-currency-list-open");
			} else {
				$(".tp-header-currency ul").removeClass("tp-currency-list-open");
			}
		});
	}

	/*======================================
	For header setting Js
	========================================*/
	if ($("#header-setting-toggle").length > 0) {
		window.addEventListener("click", function (e) {
			if (
				document.getElementById("header-setting-toggle").contains(e.target)
			) {
				$(".tp-header-setting ul").toggleClass("tp-setting-list-open");
			} else {
				$(".tp-header-setting ul").removeClass("tp-setting-list-open");
			}
		});
	}

	/*======================================
	For before-after Js
	========================================*/
	if ($(".beforeAfter").length > 0) {
		$(".beforeAfter").beforeAfter({
			movable: true,
			clickMove: true,
			position: 50,
			separatorColor: "#fafafa",
			bulletColor: "#fafafa",
			onMoveStart: function (e) {
				console.log(event.target);
			},
			onMoving: function () {
				console.log(event.target);
			},
			onMoveEnd: function () {
				console.log(event.target);
			},
		});
	}

	/*======================================
	Team slider Js
	========================================*/
	var team = new Swiper(".testimonial-active", {
		slidesPerView: 2,
		spaceBetween: 30,
		loop: true,
		roundLengths: true,
		autoplay: {
			delay: 3000,
		},
		navigation: {
			nextEl: ".testimonial-button-next",
			prevEl: ".testimonial-button-prev",
		},
		breakpoints: {
			1400: {
				slidesPerView: 3,
			},
			1200: {
				slidesPerView: 1,
			},
			992: {
				slidesPerView: 1,
			},
			768: {
				slidesPerView: 1,
			},
			576: {
				slidesPerView: 1,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	var team = new Swiper(".testimonial-active-2", {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		roundLengths: true,
		autoplay: {
			delay: 3000,
		},
		navigation: {
			nextEl: ".testimonial-button-next",
			prevEl: ".testimonial-button-prev",
		},
		breakpoints: {
			1400: {
				slidesPerView: 1,
			},
			1200: {
				slidesPerView: 1,
			},
			992: {
				slidesPerView: 1,
			},
			768: {
				slidesPerView: 1,
			},
			576: {
				slidesPerView: 1,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	var team = new Swiper(".testimonial-active-3", {
		slidesPerView: 3,
		spaceBetween: 30,
		loop: true,
		roundLengths: true,
		autoplay: {
			delay: 3000,
		},
		pagination: {
			el: ".bd-swiper-dot",
			clickable: true,
		},
		navigation: {
			nextEl: ".testimonial-button-next",
			prevEl: ".testimonial-button-prev",
		},
		breakpoints: {
			1400: {
				slidesPerView: 3,
			},
			1200: {
				slidesPerView: 3,
			},
			992: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 2,
			},
			576: {
				slidesPerView: 1,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	/*======================================
	Review slider Js
	========================================*/
	var review = new Swiper(".review-active", {
		slidesPerView: 2,
		spaceBetween: 30,
		loop: true,
		roundLengths: true,
		autoplay: {
			delay: 3000,
		},
		navigation: {
			nextEl: ".testimonial-button-next",
			prevEl: ".testimonial-button-prev",
		},
		breakpoints: {
			1400: {
				slidesPerView: 2,
			},
			1200: {
				slidesPerView: 1,
			},
			992: {
				slidesPerView: 1,
			},
			768: {
				slidesPerView: 1,
			},
			576: {
				slidesPerView: 1,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	var review = new Swiper(".review-active", {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		roundLengths: true,
		observer: true,
		observeParents: true,
		autoplay: {
			delay: 3000,
		},
		navigation: {
			nextEl: ".review-button-prev",
			prevEl: ".review-button-next",
		},
	});

	$(".review-active-two").slick({
		infinite: true,
		vertical: true,
		speed: 1000,
		autoplaySpeed: 2000,
		slidesToShow: 1,
		autoplay: true,
		arrows: true,
		prevArrow:
			'<button type="button" class="slick-prev"><i class="fa-regular fa-chevron-left"></i></button>',
		nextArrow:
			'<button type="button" class="slick-next"><i class="fa-regular fa-chevron-right"></i></button>',
		appendArrows: $(".review-slider-navigation"),
		slidesToShow: 1,
		slidesToScroll: 1,
		responsive: [
			{
				breakpoint: 1400,
				slidesToShow: 1,
			},
			{
				breakpoint: 1200,
				slidesToShow: 1,
			},
			{
				breakpoint: 992,
				slidesToShow: 1,
			},
			{
				breakpoint: 768,
				settings: {
					slidesToShow: 1,
				},
			},
			{
				breakpoint: 480,
				settings: {
					centerMode: false,
					slidesToShow: 1,
				},
			},
		],
	});

	/*======================================
	product slider Js
	========================================*/
	var product = new Swiper(".product-active", {
		slidesPerView: 4,
		spaceBetween: 15,
		loop: true,
		roundLengths: true,
		autoplay: {
			delay: 3000,
		},
		pagination: {
			el: ".bd-swiper-dot",
			clickable: true,
		},
		breakpoints: {
			1200: {
				slidesPerView: 4,
			},
			992: {
				slidesPerView: 3,
			},
			768: {
				slidesPerView: 3,
			},
			576: {
				slidesPerView: 2,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	var product = new Swiper(".furuniture-active", {
		slidesPerView: 4,
		spaceBetween: 15,
		loop: true,
		roundLengths: true,
		autoplay: {
			delay: 3000,
		},
		pagination: {
			el: ".bd-swiper-dot",
			clickable: true,
		},
		navigation: {
			nextEl: ".discount-slider-button-prev",
			prevEl: ".discount-slider-button-next",
		},
		breakpoints: {
			1200: {
				slidesPerView: 4,
			},
			992: {
				slidesPerView: 3,
			},
			768: {
				slidesPerView: 3,
			},
			576: {
				slidesPerView: 2,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	var product = new Swiper(".f-category-active", {
		slidesPerView: 5,
		spaceBetween: 15,
		loop: true,
		roundLengths: true,
		autoplay: {
			delay: 3000,
		},
		pagination: {
			el: ".bd-swiper-dot",
			clickable: true,
		},
		navigation: {
			nextEl: ".discount-slider-button-prev",
			prevEl: ".discount-slider-button-next",
		},
		breakpoints: {
			1200: {
				slidesPerView: 5,
			},
			992: {
				slidesPerView: 3,
			},
			768: {
				slidesPerView: 3,
			},
			576: {
				slidesPerView: 2,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	var productTwo = new Swiper(".discount-active", {
		slidesPerView: 5,
		spaceBetween: 15,
		loop: true,
		roundLengths: true,
		observer: true,
		observeParents: true,
		autoplay: {
			delay: 3000,
		},
		pagination: {
			el: ".bd-swiper-dot",
			clickable: true,
		},
		navigation: {
			nextEl: ".discount-slider-button-prev",
			prevEl: ".discount-slider-button-next",
		},
		breakpoints: {
			1400: {
				slidesPerView: 5,
			},
			1200: {
				slidesPerView: 4,
			},
			992: {
				slidesPerView: 4,
			},
			768: {
				slidesPerView: 3,
			},
			576: {
				slidesPerView: 2,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	/*======================================
	brand slider Js
	========================================*/
	var brand = new Swiper(".brand-active", {
		slidesPerView: 5,
		spaceBetween: 30,
		loop: true,
		autoplay: {
			delay: 3000,
		},
		breakpoints: {
			1400: {
				slidesPerView: 5,
			},
			1200: {
				slidesPerView: 4,
			},
			992: {
				slidesPerView: 4,
			},
			768: {
				slidesPerView: 3,
			},
			576: {
				slidesPerView: 2,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	/*======================================
	service slider Js
	========================================*/
	var service = new Swiper(".service-active-2", {
		slidesPerView: 3,
		spaceBetween: 30,
		loop: true,
		autoplay: {
			delay: 3000,
		},
		pagination: {
			el: ".bd-swiper-dot",
			clickable: true,
		},
		breakpoints: {
			1200: {
				slidesPerView: 3,
			},
			992: {
				slidesPerView: 3,
			},
			768: {
				slidesPerView: 2,
			},
			576: {
				slidesPerView: 1,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	var project = new Swiper(".project-active", {
		slidesPerView: 3,
		spaceBetween: 30,
		loop: true,
		autoplay: {
			delay: 3000,
		},
		breakpoints: {
			1200: {
				slidesPerView: 3,
			},
			992: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 2,
			},
			576: {
				slidesPerView: 2,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	/*======================================
	doctor slider Js
	========================================*/
	var doctor = new Swiper(".doctor-slider-active", {
		slidesPerView: 3,
		spaceBetween: 30,
		loop: true,
		autoplay: {
			delay: 3000,
		},
		navigation: {
			nextEl: ".doctor-slider-button-next",
			prevEl: ".doctor-slider-button-prev",
		},
		pagination: {
			el: ".bd-swiper-dot",
			clickable: true,
		},
		breakpoints: {
			1200: {
				slidesPerView: 3,
			},
			992: {
				slidesPerView: 2,
			},
			768: {
				slidesPerView: 2,
			},
			576: {
				slidesPerView: 1,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	/*======================================
	slider slider Js
	========================================*/
	if (jQuery(".slider-active").length > 0) {
		let sliderActive1 = ".slider-active";
		let sliderInit1 = new Swiper(sliderActive1, {
			// Optional parameters
			slidesPerView: 1,
			slidesPerColumn: 1,
			paginationClickable: true,
			fadeEffect: {
				crossFade: true,
			},
			loop: true,
			effect: "fade",
			autoplay: {
				delay: 5000,
			},
			navigation: {
				nextEl: ".slider-button-prev",
				prevEl: ".slider-button-next",
			},
			pagination: {
				el: ".banner-dot-2",
				clickable: true,
			},
			a11y: false,
		});

		function animated_swiper(selector, init) {
			let animated = function animated() {
				$(selector + " [data-animation]").each(function () {
					let anim = $(this).data("animation");
					let delay = $(this).data("delay");
					let duration = $(this).data("duration");

					$(this)
						.removeClass("anim" + anim)
						.addClass(anim + " animated")
						.css({
							webkitAnimationDelay: delay,
							animationDelay: delay,
							webkitAnimationDuration: duration,
							animationDuration: duration,
						})
						.one(
							"webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",
							function () {
								$(this).removeClass(anim + " animated");
							}
						);
				});
			};
			animated();
			// Make animated when slide change
			init.on("slideChange", function () {
				$(sliderActive1 + " [data-animation]").removeClass("animated");
			});
			init.on("slideChange", animated);
		}

		animated_swiper(sliderActive1, sliderInit1);
	}

	if (jQuery(".banner-active").length > 0) {
		let sliderActive1 = ".banner-active";
		let sliderInit1 = new Swiper(sliderActive1, {
			// Optional parameters
			slidesPerView: 1,
			slidesPerColumn: 1,
			paginationClickable: true,
			fadeEffect: {
				crossFade: true,
			},
			loop: true,
			effect: "fade",
			autoplay: {
				delay: 5000,
			},
			navigation: {
				nextEl: ".slider__button-prev",
				prevEl: ".slider__button-next",
			},
			pagination: {
				el: ".banner-dot",
				clickable: true,
			},
			a11y: false,
		});

		function animated_swiper(selector, init) {
			let animated = function animated() {
				$(selector + " [data-animation]").each(function () {
					let anim = $(this).data("animation");
					let delay = $(this).data("delay");
					let duration = $(this).data("duration");

					$(this)
						.removeClass("anim" + anim)
						.addClass(anim + " animated")
						.css({
							webkitAnimationDelay: delay,
							animationDelay: delay,
							webkitAnimationDuration: duration,
							animationDuration: duration,
						})
						.one(
							"webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",
							function () {
								$(this).removeClass(anim + " animated");
							}
						);
				});
			};
			animated();
			// Make animated when slide change
			init.on("slideChange", function () {
				$(sliderActive1 + " [data-animation]").removeClass("animated");
			});
			init.on("slideChange", animated);
		}

		animated_swiper(sliderActive1, sliderInit1);
	}

	var team = new Swiper(".banner-active-grocery", {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		roundLengths: true,
		autoplay: {
			delay: 3000,
		},
	});

	/*======================================
	Postbox slider Js
	========================================*/
	var postboxSlider = new Swiper(".postbox__slider", {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		autoplay: {
			delay: 3000,
		},
		// Navigation arrows
		navigation: {
			nextEl: ".postbox-slider-button-next",
			prevEl: ".postbox-slider-button-prev",
		},
		breakpoints: {
			1200: {
				slidesPerView: 1,
			},
			992: {
				slidesPerView: 1,
			},
			768: {
				slidesPerView: 1,
			},
			576: {
				slidesPerView: 1,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	/*======================================
	whyChoose slider Js
	========================================*/
	var whyChoose = new Swiper(".why-choose-active", {
		slidesPerView: 1,
		spaceBetween: 0,
		loop: true,
		autoplay: {
			delay: 3000,
		},
		pagination: {
			el: ".bd-swiper-dot",
			clickable: true,
		},
		breakpoints: {
			1200: {
				slidesPerView: 3,
			},
			992: {
				slidesPerView: 3,
			},
			768: {
				slidesPerView: 1,
			},
			576: {
				slidesPerView: 1,
			},
			0: {
				slidesPerView: 1,
			},
		},
	});

	// Coundawn area start here ***
	var targetDate = new Date("2024-05-12 00:00:00").getTime();

	var countdownInterval = setInterval(function () {
		var currentDate = new Date().getTime();
		var remainingTime = targetDate - currentDate;

		if (remainingTime <= 0) {
			clearInterval(countdownInterval);
			// Display a message or perform any action when the countdown timer reaches zero
			$("#countdown-container").text("Countdown has ended!");
		} else {
			var days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
			var hours = Math.floor(
				(remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
			);
			var minutes = Math.floor(
				(remainingTime % (1000 * 60 * 60)) / (1000 * 60)
			);
			var seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

			// Pad single-digit values with leading zeros
			$("#day").text(days.toString().padStart(2, "0"));
			$("#hour").text(hours.toString().padStart(2, "0"));
			$("#min").text(minutes.toString().padStart(2, "0"));
			$("#sec").text(seconds.toString().padStart(2, "0"));
		}
	}, 1000);
	// Coundawn area end here ***

	/*======================================
	22. TEAM ACTIVE
	========================================*/
	$(document).on("mouseover", ".why-choose-item", function () {
		$(".why-choose-item").removeClass("active");
		$(this).addClass("active");
	});

	/*======================================
	Countdown slider Js
	========================================*/
	if ($(".countdown-wrapper").length > 0) {
		// Function to update the countdown timer
		function updateCountdown() {
			const second = 1000,
				minute = second * 60,
				hour = minute * 60,
				day = hour * 24;

			let today = new Date();
			let dd = String(today.getDate()).padStart(2, "0");
			let mm = String(today.getMonth() + 1).padStart(2, "0");
			let yyyy = today.getFullYear();
			let nextYear = yyyy + 1;
			let dayMonth = "12/30/";
			let birthday = dayMonth + yyyy;

			today = mm + "/" + dd + "/" + yyyy;
			if (today > birthday) {
				birthday = dayMonth + nextYear;
			}

			const countDownDate = new Date(birthday).getTime();

			const x = setInterval(function () {
				const now = new Date().getTime();
				const distance = countDownDate - now;

				const days = Math.floor(distance / day);
				const hours = Math.floor((distance % day) / hour);
				const minutes = Math.floor((distance % hour) / minute);
				const seconds = Math.floor((distance % minute) / second);

				// Update the HTML elements
				document.getElementById("days").innerText = days;
				document.getElementById("hours").innerText = hours;
				document.getElementById("minutes").innerText = minutes;
				document.getElementById("seconds").innerText = seconds;

				// Check if the countdown is over
				if (distance < 0) {
					clearInterval(x);
					document.getElementById("headline").innerText =
						"It's my birthday!";
					document.getElementById("countdown").style.display = "none";
				}
			}, 1000); // Update every 1 second
		}

		// Call the updateCountdown function when the page loads
		window.onload = updateCountdown;
	}
})(jQuery);
