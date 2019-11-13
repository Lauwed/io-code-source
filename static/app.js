/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/scripts/app.js":
/*!****************************!*\
  !*** ./src/scripts/app.js ***!
  \****************************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _components_animations__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./components/animations */ "./src/scripts/components/animations.js");
/* harmony import */ var _components_animations__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_components_animations__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _components_language__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./components/language */ "./src/scripts/components/language.js");
/* harmony import */ var _components_language__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_components_language__WEBPACK_IMPORTED_MODULE_1__);



/***/ }),

/***/ "./src/scripts/components/animations.js":
/*!**********************************************!*\
  !*** ./src/scripts/components/animations.js ***!
  \**********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

var circles = document.querySelector('.circles');
var circlesEl = document.querySelectorAll('.circles__el');
var link = document.querySelector('.link-anim');
var existLink = document.getElementsByClassName('link-anim');
var linkTransition = document.querySelector('.link__page');
var existTransition = document.getElementsByClassName('link__page'); // Anim trigger => link-anim

if (existLink.length > 0) {
  link.addEventListener('click', function (e) {
    var lastCircle = circlesEl[0];
    circles.classList.add('anim--on');
    document.body.classList.add('animation');
    var currentLink = this.href;
    lastCircle.addEventListener('transitionend', function () {
      window.location = currentLink;
    });
    e.preventDefault();
  });
}

;

if (existTransition.length > 0) {
  linkTransition.addEventListener('click', function (e) {
    anim('fade-out', 'animationend', 'document.body');
  });
}

function anim(animName, type, el) {
  var currentLink = this.href;
  document.body.classList.add(animName);
  el.addEventListener(type, function () {
    window.location = currentLink;
  });
}

/***/ }),

/***/ "./src/scripts/components/language.js":
/*!********************************************!*\
  !*** ./src/scripts/components/language.js ***!
  \********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

var btn = document.querySelector('.dropdown__btn');
var content = document.querySelector('.dropdown');
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

/***/ }),

/***/ "./src/styles/app.scss":
/*!*****************************!*\
  !*** ./src/styles/app.scss ***!
  \*****************************/
/*! no static exports found */
/***/ (function(module, exports) {

// removed by extract-text-webpack-plugin

/***/ }),

/***/ 0:
/*!********************************************************!*\
  !*** multi ./src/scripts/app.js ./src/styles/app.scss ***!
  \********************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(/*! /Users/antoineweverbergh/Desktop/heaj/IO/io_interface/src/scripts/app.js */"./src/scripts/app.js");
module.exports = __webpack_require__(/*! /Users/antoineweverbergh/Desktop/heaj/IO/io_interface/src/styles/app.scss */"./src/styles/app.scss");


/***/ })

/******/ });
//# sourceMappingURL=app.js.map