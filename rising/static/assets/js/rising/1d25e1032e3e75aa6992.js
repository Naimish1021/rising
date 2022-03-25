(window.webpackJsonp = window.webpackJsonp || []).push([
    [18], {
        1197: function(t, n, e) {
            "use strict";
            var o = e(620),
                l = e.n(o);
            n.default = l.a
        },
        1198: function(t, n, e) {
            (n = e(97)(!1)).push([t.i, "", ""]), t.exports = n
        },
        1563: function(t, n, e) {
            "use strict";
            e.r(n);
            var o = e(99),
                l = e(51),
                r = e.n(l),
                c = e(148),
                m = e(424),
                h = e(444),
                f = e(431);
            function d() {
                var data = Object(o.a)(["\n        query Downloads($offset: Int = 0) {\n          downloads(limit: 20, offset: $offset, order_by: { id: asc }) {\n            id\n            path\n            name\n          }\n        }\n      "]);
                return d = function() {
                    return data
                }, data
            }
            var _ = {
                    components: {
                        MasterHeader: m.a,
                        MasterFooter: h.a,
                        HeroStatic: f.a
                    },
                    apollo: {
                        downloads: {
                            query: r()(d()),
                            variables: function() {
                                return {
                                    offset: 0
                                }
                            }
                        }
                    },
                    methods: {
                        storageUrl: c.e
                    }
                },
                v = e(1197),
                k = e(50);
            var component = Object(k.a)(_, (function() {
                var t = this,
                    n = t.$createElement,
                    e = t._self._c || n;
                return e("div", {
                    class: t.$style.container
                }, [e("master-header"), t._v(" "), e("hero-static", [e("h1", {
                    staticClass: "mb-1"
                }, [t._v("Downloads")]), t._v(" "), e("p", {
                    staticClass: "o60 mb-0"
                }, [t._v("\n      Important downloads, news & updates and more.\n    ")])]), t._v(" "), e("div", {
                    staticClass: "container py-5"
                }, [e("ul", {
                    staticClass: "list-unstyled"
                }, t._l(t.downloads, (function(n, o) {
                    return e("li", {
                        key: o,
                        staticClass: "mb-2"
                    }, [e("a", {
                        attrs: {
                            href: t.storageUrl(n.path),
                            download: n.name,
                            target: "_blank"
                        }
                    }, [e("i", {
                        staticClass: "uil uil-import"
                    }), t._v(" "), e("span", {
                        staticClass: "text-body"
                    }, [t._v(t._s(n.name))])])])
                })), 0)]), t._v(" "), e("master-footer")], 1)
            }), [], !1, (function(t) {
                this.$style = v.default.locals || v.default
            }), null, null);
            n.default = component.exports
        },
        418: function(t, n, e) {
            var content = e(427);
            "string" == typeof content && (content = [
                [t.i, content, ""]
            ]), content.locals && (t.exports = content.locals);
            (0, e(98).default)("8682140c", content, !0, {
                sourceMap: !1
            })
        },
        419: function(t, n, e) {
            var content = e(429);
            "string" == typeof content && (content = [
                [t.i, content, ""]
            ]), content.locals && (t.exports = content.locals);
            (0, e(98).default)("51eba5b0", content, !0, {
                sourceMap: !1
            })
        },
        420: function(t, n, e) {
            var content = e(437);
            "string" == typeof content && (content = [
                [t.i, content, ""]
            ]), content.locals && (t.exports = content.locals);
            (0, e(98).default)("fe89f6b0", content, !0, {
                sourceMap: !1
            })
        },
        421: function(t, n, e) {
            "use strict";
            var o = e(99),
                l = e(51),
                r = e.n(l),
                c = e(66);
            function m() {
                var data = Object(o.a)(["\n        query Me($id: Int!) {\n          users_by_pk(id: $id) {\n            id\n            first_name\n            last_name\n            role\n            email\n            phone\n            gender\n            dob\n            avatar\n          }\n        }\n      "]);
                return m = function() {
                    return data
                }, data
            }
            n.a = {
                apollo: {
                    user: {
                        query: r()(m()),
                        variables: function() {
                            return {
                                id: this.token["https://hasura.io/jwt/claims"]["x-hasura-user-id"]
                            }
                        },
                        update: function(data) {
                            return data.users_by_pk
                        },
                        skip: function() {
                            return !this.isLoggedIn
                        }
                    }
                },
                computed: {
                    isLoggedIn: function() {
                        return Boolean(this.$apolloHelpers.getToken())
                    },
                    token: function() {
                        return Object(c.a)(this.$apolloHelpers.getToken())
                    },
                    isMasterAdmin: function() {
                        return this.user && this.user.id <= 30
                    }
                },
                methods: {
                    onLogout: function() {
                        this.$apolloHelpers.onLogout(), window.location.href = "/"
                    }
                }
            }
        },
        423: function(t, n, e) {
            var content = e(447);
            "string" == typeof content && (content = [
                [t.i, content, ""]
            ]), content.locals && (t.exports = content.locals);
            (0, e(98).default)("2bad8496", content, !0, {
                sourceMap: !1
            })
        },
        424: function(t, n, e) {
            "use strict";
            var o = e(432),
                l = e(434),
                r = e(421),
                c = {
                    components: {
                        SlideXRightTransition: o.a
                    },
                    mixins: [r.a, l.a],
                    data: function() {
                        return {
                            showHamburger: !1
                        }
                    },
                    destroyed: function() {
                        this.clickOutHandler()
                    },
                    methods: {
                        onToggleHamburger: function() {
                            this.showHamburger = !this.showHamburger, this.showHamburger ? (this.listenForClickOut = !0, window.document.body.classList.add("menu-open")) : (this.listenForClickOut = !1, window.document.body.classList.remove("menu-open"))
                        },
                        clickOutHandler: function() {
                            this.showHamburger && (this.showHamburger = !1, window.document.body.classList.remove("menu-open"))
                        }
                    }
                },
                m = e(426),
                h = e(50);
            var component = Object(h.a)(c, (function() {
                var t = this,
                    n = t.$createElement,
                    o = t._self._c || n;
                return o("header", {
                    class: t.$style.container
                }, [o("div", {
                    staticClass: "container"
                }, [o("nuxt-link", {
                    class: t.$style.logo,
                    attrs: {
                        to: {
                            name: "index"
                        }
                    }
                }, [o("img", {
                    attrs: {
                        src: e(425),
                        alt: "Invincible NGO",
                        height: "32"
                    }
                })]), t._v(" "), o("button", {
                    class: ["btn", t.$style.btnHamburger, t.showHamburger ? t.$style.open : null],
                    attrs: {
                        type: "button"
                    },
                    on: {
                        click: t.onToggleHamburger
                    }
                }, [o("span"), t._v(" "), o("span"), t._v(" "), o("span")]), t._v(" "), o("slide-x-right-transition", [t.showHamburger ? o("div", {
                    class: t.$style.mobileMenuContainer
                }, [o("ul", {
                    class: ["list-unstyled", t.$style.menuItems]
                }, [t.isLoggedIn ? [o("li", [o("nuxt-link", {
                    attrs: {
                        to: {
                            name: "dashboard"
                        }
                    },
                    nativeOn: {
                        click: function(n) {
                            return t.clickOutHandler(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-list-ul"
                }), t._v("\n                Dashboard\n              ")])], 1), t._v(" "), o("li", [o("nuxt-link", {
                    attrs: {
                        to: {
                            name: "dashboard-profile"
                        }
                    },
                    nativeOn: {
                        click: function(n) {
                            return t.clickOutHandler(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-user"
                }), t._v("\n                My Profile\n              ")])], 1), t._v(" "), o("li", [o("a", {
                    attrs: {
                        href: "#"
                    },
                    on: {
                        click: function(n) {
                            return n.preventDefault(), t.onLogout(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-power"
                }), t._v("\n                Logout\n              ")])])] : t._e(), t._v(" "), o("li", [o("nuxt-link", {
                    attrs: {
                        to: {
                            name: "index"
                        }
                    },
                    nativeOn: {
                        click: function(n) {
                            return t.clickOutHandler(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-home"
                }), t._v("\n              Home\n            ")])], 1), t._v(" "), o("li", [o("nuxt-link", {
                    attrs: {
                        to: {
                            name: "events"
                        }
                    },
                    nativeOn: {
                        click: function(n) {
                            return t.clickOutHandler(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-mountains-sun"
                }), t._v("\n              Events\n            ")])], 1), t._v(" "), o("li", [o("nuxt-link", {
                    attrs: {
                        to: {
                            name: "downloads"
                        }
                    },
                    nativeOn: {
                        click: function(n) {
                            return t.clickOutHandler(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-import"
                }), t._v("\n              Downloads\n            ")])], 1), t._v(" "), o("li", [o("nuxt-link", {
                    attrs: {
                        to: {
                            name: "about"
                        }
                    },
                    nativeOn: {
                        click: function(n) {
                            return t.clickOutHandler(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-building"
                }), t._v("\n              About\n            ")])], 1), t._v(" "), o("li", [o("nuxt-link", {
                    attrs: {
                        to: {
                            name: "team-type"
                        }
                    },
                    nativeOn: {
                        click: function(n) {
                            return t.clickOutHandler(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-users-alt"
                }), t._v("\n              Team\n            ")])], 1), t._v(" "), t.isLoggedIn ? t._e() : o("li", [o("nuxt-link", {
                    attrs: {
                        to: {
                            name: "login",
                            query: {
                                redirect: "/dashboard"
                            }
                        }
                    },
                    nativeOn: {
                        click: function(n) {
                            return t.clickOutHandler(n)
                        }
                    }
                }, [o("i", {
                    staticClass: "uil uil-user"
                }), t._v("\n              Login\n            ")])], 1)], 2), t._v(" "), o("hr"), t._v(" "), o("div", {
                    class: t.$style.contact
                }, [o("h6", {
                    staticClass: "text-primary mb-3"
                }, [t._v("Contact")]), t._v(" "), o("a", {
                    staticClass: "d-block text-body mb-1",
                    attrs: {
                        href: "tel:+919099400699"
                    }
                }, [o("i", {
                    staticClass: "uil uil-phone"
                }), t._v(" +91 9099 400 699")]), t._v(" "), o("a", {
                    staticClass: "d-block text-body mb-1",
                    attrs: {
                        href: "tel:+919913800699"
                    }
                }, [o("i", {
                    staticClass: "uil uil-phone"
                }), t._v(" +91 9913 800 699")]), t._v(" "), o("a", {
                    staticClass: "d-block text-body",
                    attrs: {
                        href: "mailto:info@invinciblengo.org"
                    }
                }, [o("i", {
                    staticClass: "uil uil-at"
                }), t._v(" info@invinciblengo.org")]), t._v(" "), o("ul", {
                    class: ["list-inline mt-4 mb-0", t.$style.socialContacts]
                }, [o("li", {
                    staticClass: "list-inline-item"
                }, [o("a", {
                    attrs: {
                        href: "https://www.instagram.com/invinciblengo",
                        target: "_blank",
                        rel: "nofollow noopener"
                    }
                }, [o("i", {
                    staticClass: "uil uil-instagram"
                })])]), t._v(" "), o("li", {
                    staticClass: "list-inline-item"
                }, [o("a", {
                    attrs: {
                        href: "https://www.facebook.com/invinciblengo",
                        target: "_blank",
                        rel: "nofollow noopener"
                    }
                }, [o("i", {
                    staticClass: "uil uil-facebook-f"
                })])]), t._v(" "), o("li", {
                    staticClass: "list-inline-item"
                }, [o("a", {
                    attrs: {
                        href: "https://www.youtube.com/channel/UCw8uaiUJgCJFHfvLVgZwAww",
                        target: "_blank",
                        rel: "nofollow noopener"
                    }
                }, [o("i", {
                    staticClass: "uil uil-youtube"
                })])]), t._v(" "), o("li", {
                    staticClass: "list-inline-item"
                }, [o("a", {
                    attrs: {
                        href: "https://wa.me/919099400699",
                        target: "_blank",
                        rel: "nofollow noopener"
                    }
                }, [o("i", {
                    staticClass: "uil uil-whatsapp"
                })])]), t._v(" "), o("li", {
                    staticClass: "list-inline-item"
                }, [o("a", {
                    attrs: {
                        href: "https://g.page/invinciblengo?share",
                        target: "_blank",
                        rel: "nofollow noopener"
                    }
                }, [o("i", {
                    staticClass: "uil uil-map-marker"
                })])])])])]) : t._e()])], 1)])
            }), [], !1, (function(t) {
                this.$style = m.default.locals || m.default
            }), null, null);
            n.a = component.exports
        },
        425: function(t, n, e) {
            t.exports = e.p + "img/1a82462.svg"
        },
        426: function(t, n, e) {
            "use strict";
            var o = e(418),
                l = e.n(o);
            n.default = l.a
        },
        427: function(t, n, e) {
            (n = e(97)(!1)).push([t.i, ".menu-open{overflow:hidden}.container_1vhpE{position:absolute;top:0;left:0;right:0;z-index:1030;padding-top:1rem;padding-bottom:1rem}.container_1vhpE .logo_1Zlqi{display:inline-block;line-height:44px}.container_1vhpE .btnHamburger_2i064{position:relative;height:44px;width:44px;float:right;z-index:10}.container_1vhpE .btnHamburger_2i064:focus{box-shadow:none!important}.container_1vhpE .btnHamburger_2i064>span{display:block;height:2px;width:18px;background:#fff;position:absolute;left:10px;-webkit-transition:all .3s;transition:all .3s}.container_1vhpE .btnHamburger_2i064>span:first-child{top:14px;-webkit-transform-origin:100% 0;transform-origin:100% 0}.container_1vhpE .btnHamburger_2i064>span:nth-child(2){top:20px}.container_1vhpE .btnHamburger_2i064>span:nth-child(3){top:26px;-webkit-transform-origin:100% 100%;transform-origin:100% 100%}.container_1vhpE .btnHamburger_2i064.open_3PHG2>span{background:#1c1c1c}.container_1vhpE .btnHamburger_2i064.open_3PHG2>span:first-child{-webkit-transform:rotate(-45deg);transform:rotate(-45deg)}.container_1vhpE .btnHamburger_2i064.open_3PHG2>span:nth-child(2){-webkit-transform:translateX(30px);transform:translateX(30px);opacity:0}.container_1vhpE .btnHamburger_2i064.open_3PHG2>span:nth-child(3){-webkit-transform:rotate(45deg);transform:rotate(45deg)}.container_1vhpE .mobileMenuContainer_16d8U{position:fixed;right:0;top:0;bottom:0;min-width:300px;background:#fff;box-shadow:0 0 500px 1000px rgba(0,0,0,.4);display:-webkit-box;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;flex-direction:column;-webkit-box-pack:justify;justify-content:space-between}.container_1vhpE .mobileMenuContainer_16d8U .menuItems_3ZQHf{padding:4rem 1.5rem 1.5rem}.container_1vhpE .mobileMenuContainer_16d8U .menuItems_3ZQHf a{display:block;color:#1c1c1c;padding:.5rem 0}.container_1vhpE .mobileMenuContainer_16d8U .menuItems_3ZQHf a>i{color:#de5824;font-size:1.5rem;margin-right:.5rem;vertical-align:-2px}.container_1vhpE .mobileMenuContainer_16d8U .contact_APAPz{padding:1.5rem;border-top:1px solid #e3e3e3}.container_1vhpE .mobileMenuContainer_16d8U .contact_APAPz .socialContacts_1zZf7 a{background:#f1f1f1;width:38px;height:38px;display:-webkit-box;display:flex;-webkit-box-align:center;align-items:center;-webkit-box-pack:center;justify-content:center;border-radius:50%;color:#000;font-size:1.5rem}", ""]), n.locals = {
                container: "container_1vhpE",
                logo: "logo_1Zlqi",
                btnHamburger: "btnHamburger_2i064",
                open: "open_3PHG2",
                mobileMenuContainer: "mobileMenuContainer_16d8U",
                menuItems: "menuItems_3ZQHf",
                contact: "contact_APAPz",
                socialContacts: "socialContacts_1zZf7"
            }, t.exports = n
        },
        428: function(t, n, e) {
            "use strict";
            var o = e(419),
                l = e.n(o);
            n.default = l.a
        },
        429: function(t, n, e) {
            (n = e(97)(!1)).push([t.i, ".container_1n8qm{padding-top:calc(76px + 2rem);padding-bottom:2rem;background:#de5824;color:#fff}", ""]), n.locals = {
                container: "container_1n8qm"
            }, t.exports = n
        },
        431: function(t, n, e) {
            "use strict";
            var o = {},
                l = e(428),
                r = e(50);
            var component = Object(r.a)(o, (function() {
                var t = this.$createElement,
                    n = this._self._c || t;
                return n("div", {
                    class: this.$style.container
                }, [n("div", {
                    staticClass: "container"
                }, [this._t("default")], 2)])
            }), [], !1, (function(t) {
                this.$style = l.default.locals || l.default
            }), null, null);
            n.a = component.exports
        },
        432: function(t, n, e) {
            "use strict";
            var o = {
                    name: "slide-x-right-transition",
                    mixins: [{
                        inheritAttrs: !1,
                        props: {
                            duration: {
                                type: [Number, Object],
                                default: 300
                            },
                            delay: {
                                type: [Number, Object],
                                default: 0
                            },
                            group: Boolean,
                            tag: {
                                type: String,
                                default: "span"
                            },
                            origin: {
                                type: String,
                                default: ""
                            },
                            styles: {
                                type: Object,
                                default: () => ({
                                    animationFillMode: "both",
                                    animationTimingFunction: "ease-out"
                                })
                            }
                        },
                        computed: {
                            componentType() {
                                return this.group ? "transition-group" : "transition"
                            },
                            hooks() {
                                return {
                                    beforeEnter: this.beforeEnter,
                                    afterEnter: this.cleanUpStyles,
                                    beforeLeave: this.beforeLeave,
                                    leave: this.leave,
                                    afterLeave: this.cleanUpStyles,
                                    ...this.$listeners
                                }
                            }
                        },
                        methods: {
                            beforeEnter(t) {
                                let n = this.duration.enter ? this.duration.enter : this.duration;
                                t.style.animationDuration = `${n}ms`;
                                let e = this.delay.enter ? this.delay.enter : this.delay;
                                t.style.animationDelay = `${e}ms`, this.setStyles(t)
                            },
                            cleanUpStyles(t) {
                                Object.keys(this.styles).forEach(n => {
                                    this.styles[n] && (t.style[n] = "")
                                }), t.style.animationDuration = "", t.style.animationDelay = ""
                            },
                            beforeLeave(t) {
                                let n = this.duration.leave ? this.duration.leave : this.duration;
                                t.style.animationDuration = `${n}ms`;
                                let e = this.delay.leave ? this.delay.leave : this.delay;
                                t.style.animationDelay = `${e}ms`, this.setStyles(t)
                            },
                            leave(t) {
                                this.setAbsolutePosition(t)
                            },
                            setStyles(t) {
                                this.setTransformOrigin(t), Object.keys(this.styles).forEach(n => {
                                    const e = this.styles[n];
                                    e && (t.style[n] = e)
                                })
                            },
                            setAbsolutePosition(t) {
                                return this.group && (t.style.position = "absolute"), this
                            },
                            setTransformOrigin(t) {
                                return this.origin && (t.style.transformOrigin = this.origin), this
                            }
                        }
                    }],
                    props: {
                        styles: {
                            type: Object,
                            default: function() {
                                return {
                                    animationFillMode: "both",
                                    animationTimingFunction: "cubic-bezier(.25,.8,.50,1)"
                                }
                            }
                        }
                    }
                },
                l = (e(436), e(50)),
                component = Object(l.a)(o, (function() {
                    var t = this.$createElement;
                    return (this._self._c || t)(this.componentType, this._g(this._b({
                        tag: "component",
                        attrs: {
                            tag: this.tag,
                            "enter-active-class": "slideXRightIn",
                            "move-class": "slide-move",
                            "leave-active-class": "slideXRightOut"
                        }
                    }, "component", this.$attrs, !1), this.hooks), [this._t("default")], 2)
                }), [], !1, null, null, null);
            n.a = component.exports
        },
        434: function(t, n, e) {
            "use strict";
            var o = e(2),
                l = e(12);
            n.a = {
                data: function() {
                    return {
                        listenForClickOut: !1
                    }
                },
                watch: {
                    listenForClickOut: function(t, n) {
                        t !== n && (Object(l.c)(this.clickOutElement, this.clickOutEventName, this._clickOutHandler, l.a), t && Object(l.d)(this.clickOutElement, this.clickOutEventName, this._clickOutHandler, l.a))
                    }
                },
                beforeCreate: function() {
                    this.clickOutElement = null, this.clickOutEventName = null
                },
                mounted: function() {
                    this.clickOutElement || (this.clickOutElement = document), this.clickOutEventName || (this.clickOutEventName = "click"), this.listenForClickOut && Object(l.d)(this.clickOutElement, this.clickOutEventName, this._clickOutHandler, l.a)
                },
                beforeDestroy: function() {
                    Object(l.c)(this.clickOutElement, this.clickOutEventName, this._clickOutHandler, l.a)
                },
                methods: {
                    isClickOut: function(t) {
                        return !Object(o.d)(this.$el, t.target)
                    },
                    _clickOutHandler: function(t) {
                        this.clickOutHandler && this.isClickOut(t) && this.clickOutHandler(t)
                    }
                }
            }
        },
        436: function(t, n, e) {
            "use strict";
            var o = e(420);
            e.n(o).a
        },
        437: function(t, n, e) {
            (n = e(97)(!1)).push([t.i, ".slide-move{-webkit-transition:-webkit-transform .3s;transition:-webkit-transform .3s;transition:transform .3s;transition:transform .3s,-webkit-transform .3s}@-webkit-keyframes slideXRightIn{0%{opacity:0;-webkit-transform:translateX(15px);transform:translateX(15px)}to{opacity:1}}@keyframes slideXRightIn{0%{opacity:0;-webkit-transform:translateX(15px);transform:translateX(15px)}to{opacity:1}}.slideXRightIn{-webkit-animation-name:slideXRightIn;animation-name:slideXRightIn}@-webkit-keyframes slideXRightOut{0%{opacity:1}to{opacity:0;-webkit-transform:translateX(15px);transform:translateX(15px)}}@keyframes slideXRightOut{0%{opacity:1}to{opacity:0;-webkit-transform:translateX(15px);transform:translateX(15px)}}.slideXRightOut{-webkit-animation-name:slideXRightOut;animation-name:slideXRightOut}", ""]), t.exports = n
        },
        444: function(t, n, e) {
            "use strict";
            var o = [function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("div", {
                        staticClass: "col-12 col-md-6 col-lg-4 py-3"
                    }, [n("img", {
                        staticClass: "mb-4",
                        attrs: {
                            src: e(445),
                            alt: "Invincible NGO",
                            width: "180"
                        }
                    }), this._v(" "), n("p", {
                        staticClass: "o60"
                    }, [this._v("\n          Invincible is a Non Government Organization, being run by young\n          students for social reformation and building the nation with moral\n          values and ethics.\n        ")])])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("li", [n("a", {
                        attrs: {
                            href: "https://stories.invinciblengo.org",
                            target: "_blank"
                        }
                    }, [this._v("Stories")])])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("p", {
                        staticClass: "font-size-sm o60"
                    }, [this._v("\n            308, University Plaza, Above Chocolate Room, "), n("br"), this._v("\n            Vijay Cross Roads, Navrangpura,"), n("br"), this._v("\n            Ahmedabad, Gujarat 380009\n          ")])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("a", {
                        staticClass: "d-block mb-1",
                        attrs: {
                            href: "tel:+919099400699"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-phone"
                    }), this._v(" +91 9099 400 699")])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("a", {
                        staticClass: "d-block mb-4",
                        attrs: {
                            href: "tel:+919913800699"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-phone"
                    }), this._v(" +91 9913 800 699")])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("p", {
                        staticClass: "font-size-sm o60"
                    }, [this._v("\n            407, 4th Floor, Business Corner,"), n("br"), this._v("Opp Indira Circle BRTS,"), n("br"), this._v("\n            Rajkot, Gujarat 360005\n          ")])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("a", {
                        staticClass: "d-block mb-1",
                        attrs: {
                            href: "tel:+919978650699"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-phone"
                    }), this._v(" +91 9978 650 699")])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("a", {
                        staticClass: "d-block mb-1",
                        attrs: {
                            href: "mailto:info@invinciblengo.org"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-at"
                    }), this._v(" info@invinciblengo.org")])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("li", {
                        staticClass: "list-inline-item"
                    }, [n("a", {
                        attrs: {
                            href: "https://www.facebook.com/invinciblengo",
                            target: "_blank",
                            rel: "nofollow noopener"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-facebook-f"
                    })])])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("li", {
                        staticClass: "list-inline-item"
                    }, [n("a", {
                        attrs: {
                            href: "https://www.instagram.com/invinciblengo",
                            target: "_blank",
                            rel: "nofollow noopener"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-instagram"
                    })])])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("li", {
                        staticClass: "list-inline-item"
                    }, [n("a", {
                        attrs: {
                            href: "https://www.youtube.com/channel/UCw8uaiUJgCJFHfvLVgZwAww",
                            target: "_blank",
                            rel: "nofollow noopener"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-youtube"
                    })])])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("li", {
                        staticClass: "list-inline-item"
                    }, [n("a", {
                        attrs: {
                            href: "https://wa.me/919099400699",
                            target: "_blank",
                            rel: "nofollow noopener"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-whatsapp"
                    })])])
                }, function() {
                    var t = this.$createElement,
                        n = this._self._c || t;
                    return n("li", {
                        staticClass: "list-inline-item"
                    }, [n("a", {
                        attrs: {
                            href: "https://g.page/invinciblengo?share",
                            target: "_blank",
                            rel: "nofollow noopener"
                        }
                    }, [n("i", {
                        staticClass: "uil uil-map-marker"
                    })])])
                }],
                l = e(446),
                r = e(50);
            var component = Object(r.a)({}, (function() {
                var t = this,
                    n = t.$createElement,
                    e = t._self._c || n;
                return e("footer", {
                    class: t.$style.container
                }, [e("div", {
                    staticClass: "container"
                }, [e("div", {
                    staticClass: "row"
                }, [t._m(0), t._v(" "), e("div", {
                    staticClass: "col-lg-4 py-3 d-none d-lg-block"
                }, [e("h6", {
                    staticClass: "text-primary"
                }, [t._v("Quick Links")]), t._v(" "), e("ul", {
                    staticClass: "list-unstyled mb-0"
                }, [e("li", [e("nuxt-link", {
                    attrs: {
                        to: {
                            name: "events"
                        }
                    }
                }, [t._v("Events")])], 1), t._v(" "), e("li", [e("nuxt-link", {
                    attrs: {
                        to: {
                            name: "downloads"
                        }
                    }
                }, [t._v("Downloads")])], 1), t._v(" "), e("li", [e("nuxt-link", {
                    attrs: {
                        to: {
                            name: "login"
                        }
                    }
                }, [t._v("Login")])], 1), t._v(" "), t._m(1)])]), t._v(" "), e("div", {
                    staticClass: "col-12 col-md-6 col-lg-4 py-3"
                }, [e("div", {
                    class: t.$style.contact
                }, [e("h6", {
                    staticClass: "text-uppercase mb-2"
                }, [t._v("Contact")]), t._v(" "), e("h6", {
                    staticClass: "mb-2"
                }, [t._v("Ahmedabad")]), t._v(" "), t._m(2), t._v(" "), e("p", {
                    staticClass: "font-size-sm o60"
                }, [t._v("\n            Office Timings: 11AM to 8PM\n          ")]), t._v(" "), t._m(3), t._v(" "), t._m(4), t._v(" "), e("h6", {
                    staticClass: "mb-2"
                }, [t._v("Rajkot")]), t._v(" "), t._m(5), t._v(" "), e("p", {
                    staticClass: "font-size-sm o60"
                }, [t._v("\n            Office Timings: 11AM to 8PM\n          ")]), t._v(" "), t._m(6), t._v(" "), t._m(7), t._v(" "), e("ul", {
                    class: ["list-inline mt-4 mb-0", t.$style.socialContacts]
                }, [t._m(8), t._v(" "), t._m(9), t._v(" "), t._m(10), t._v(" "), t._m(11), t._v(" "), t._m(12)])])])]), t._v(" "), e("div", {
                    class: [t.$style.copy, "mt-4 py-5"]
                }, [t._v("\n      Â© 2013-2021 Invincible. â€¢\n      "), e("nuxt-link", {
                    attrs: {
                        to: {
                            name: "privacy"
                        }
                    }
                }, [t._v("Privacy Policy")]), t._v(" â€¢\n      "), e("nuxt-link", {
                    attrs: {
                        to: {
                            name: "term-and-conditions"
                        }
                    }
                }, [t._v("Terms and Conditions")])], 1)])])
            }), o, !1, (function(t) {
                this.$style = l.default.locals || l.default
            }), null, null);
            n.a = component.exports
        },
        445: function(t, n, e) {
            t.exports = e.p + "img/59fac0f.svg"
        },
        446: function(t, n, e) {
            "use strict";
            var o = e(423),
                l = e.n(o);
            n.default = l.a
        },
        447: function(t, n, e) {
            (n = e(97)(!1)).push([t.i, ".container_2f3P9{background:#1c1c1c;color:#fff;font-size:.875rem;padding-top:1rem}.container_2f3P9 a{color:#fff}.container_2f3P9 .stories_1MAbK a{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.container_2f3P9 .contact_1y8RE .socialContacts_kPmZ9 a{background:#f1f1f1;width:38px;height:38px;display:-webkit-box;display:flex;-webkit-box-align:center;align-items:center;-webkit-box-pack:center;justify-content:center;border-radius:50%;color:#000;font-size:1.5rem}.container_2f3P9 .copy__C-8w{border-top:1px solid hsla(0,0%,100%,.6)}", ""]), n.locals = {
                container: "container_2f3P9",
                stories: "stories_1MAbK",
                contact: "contact_1y8RE",
                socialContacts: "socialContacts_kPmZ9",
                copy: "copy__C-8w"
            }, t.exports = n
        },
        620: function(t, n, e) {
            var content = e(1198);
            "string" == typeof content && (content = [
                [t.i, content, ""]
            ]), content.locals && (t.exports = content.locals);
            (0, e(98).default)("07398c50", content, !0, {
                sourceMap: !1
            })
        }
    }
]);