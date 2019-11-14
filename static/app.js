var circles = document.querySelector('.circles');
var circlesEl = document.querySelectorAll('.circles__el');
var link = document.querySelector('.link-anim');
var existLink = document.getElementsByClassName('link-anim');
var linkTransition = document.querySelector('.link__page');
var existTransition = document.getElementsByClassName('link__page');
var factsSection = document.querySelector('.section__facts');
var formSection = document.querySelector('.section--form');
var main = document.querySelector('.main');
// Anim trigger => link-anim


// Lance l'anim des cercles
if (existLink.length > 0) {
  link.addEventListener('click', function (e) {
    const lastCircle = circlesEl[0];
    circles.classList.add('anim--on');
    main.classList.add('animation');
    const currentLink = this.href;
    lastCircle.addEventListener('transitionend', function () {
      formSection.classList.add('hide');
      factsSection.classList.remove('hide');
    });
    //e.preventDefault();
  });
};
// fade-out au changement de page
if (existTransition.length > 0) {
  linkTransition.addEventListener('click', function (e) {
    anim('fade-out', 'animationend', 'document.body');
  });
}

function anim(animName, type, el) {
  const currentLink = this.href;
  document.body.classList.add(animName);
  el.addEventListener(type, function () {
    window.location = currentLink;
  });
}

var btn = document.querySelector('.dropdown__btn');
var content = document.querySelector('.dropdown');

if (btn) {
  btn.addEventListener('click', function (e) {
    content.classList.toggle('dropdown--active');
  });

  window.onclick = function (e) {
    if (!e.target.matches('.dropdown__btn')) {
      var dropdowns = document.getElementsByClassName('dropdown');

      for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];

        if (openDropdown.classList.contains('dropdown--active')) {
          openDropdown.classList.remove('dropdown--active');
        }
      }
    }
  };
}