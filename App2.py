from reactpy import component, html, run

@component
def Website():
    return html.div(
        {
            "style": {
                "background": "linear-gradient(to bottom, #0f0f0f 85%, #091426 95%)",
                "alignItems": "center",
                "display": "flex",
                "flexDirection": "column",
                "height": "100vh",
                "width": "100vw",
                "position": "fixed",
                "left": "0",
                "right": "0",
                "top": "0",
            }
        },

        html.img(
            {
                "src": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMyp8SO4Y5v1jmEs7ZkI8SjZIVI96h_ucfow&s",
                "alt": "Robloxia Flag",
                "style": {
                    "width":"900px",
                    "borderRadius":"10px",
                    "boxShadow":"0px 4px 12px rgba(0,0,0,0.5)",
                    "position":"absolute",
                    "transform": "translate(-50%, -50%)",
                    "top":"50%",
                    "left":"50%",
                    "opacity":"0.05",
                    "zIndex":"-1",
                },
            }
        ),

        html.link(
            {
                "rel": "stylesheet",
                "href": "https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap"
            }
        ),

        html.link(
            {
                "rel": "stylesheet",
                "href": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap"
            }
        ),

        html.label(
            {
                "style": {
                    "backgroundColor": "#FFFFFF00",
                    "fontFamily": "Poppins",
                    "fontWeight": "600",
                    "color": "#FFFFFF6D",
                    "fontSize": 90,
                    "marginTop": "30px",
                    "user-select": "none",
                }
            }, 
            "Robloxia Intelligence Agency"
        ),

         html.label(
            {
                "style": {
                    "backgroundColor": "#FFFFFF00",
                    "fontFamily": "Poppins",
                    "fontWeight": "1000",
                    "color": "#FFFFFF",
                    "fontSize": 27,
                    "marginTop": "5px",
                    "user-select": "none",
                }
            }, 
            "☆ Observe. Protect. Prevail. ☆"
        ),

        html.label(
            {
                "style": {
                    "backgroundColor": "#FFFFFF00",
                    "fontFamily": "Montserrat",
                    "fontWeight": "500",
                    "color": "#FFFFFF",
                    "fontSize": 27,
                    "marginTop": "60px",
                    "user-select": "none",
                }
            }, 
            "Welcome, log in using your credentials to continue."
        ),

        html.div(
            {
                "style": {
                    "backgroundColor": "#2C2C2C",
                    "alignItems": "flex-start",
                    "display": "flex",
                    "flexDirection": "column",
                    "height": "35%",
                    "width": "45%",
                    "marginTop": "20px",
                    "borderRadius": "12px"
                }
            },

            html.label(
                {
                    "style": {
                        "backgroundColor": "#FFFFFF00",
                        "fontFamily": "Montserrat",
                        "fontWeight": "100",
                        "color": "#FFFFFF",
                        "fontSize": 23,
                        "marginTop": "20px",
                        "marginLeft": "20px",
                        "user-select": "none",
                    }
                }, 
                "Username"
            ),

            html.input(
                {
                    "type": "text",
                    "placeholder": "Enter Username",
                    "style": {
                        "backgroundColor": "#191919FF",
                        "fontFamily": "Montserrat",
                        "fontWeight": "400",
                        "color": "#FFFFFF",
                        "fontSize": 22,
                        "padding": "20px",
                        "marginTop": "10px",
                        "marginLeft": "20px",
                        "height": "5px",
                        "width": "88%",
                        "border": "none",
                        "borderRadius": "12px",
                    }
                }
            ),

            html.label(
                {
                    "style": {
                        "backgroundColor": "#FFFFFF00",
                        "fontFamily": "Montserrat",
                        "fontWeight": "100",
                        "color": "#FFFFFF",
                        "fontSize": 23,
                        "marginTop": "15px",
                        "marginLeft": "20px",
                        "user-select": "none",
                    }
                }, 
                "Password"
            ),

            html.input(
                {
                    "type": "text",
                    "placeholder": "Enter Password",
                    "style": {
                        "backgroundColor": "#191919FF",
                        "fontFamily": "Montserrat",
                        "fontWeight": "400",
                        "color": "#FFFFFF",
                        "fontSize": 22,
                        "padding": "20px",
                        "marginTop": "10px",
                        "marginLeft": "20px",
                        "height": "5px",
                        "width": "88%",
                        "border": "none",
                        "borderRadius": "12px"
                    }
                }
            ),
        ),

     html.div(
            {
                "style": {
                    "backgroundColor": "#FFFFFF00",
                    "justifyContent": "center",
                    "display": "flex",
                    "flexDirection": "row",
                    "height": "5%",
                    "width": "45%",
                    "marginTop": "20px",
                    "gap":"70px"
                }
            },

            html.label(
                {
                    "style": {
                        "backgroundColor": "#FFFFFF00",
                        "fontFamily": "Montserrat",
                        "fontWeight": "100",
                        "color": "#FFFFFF",
                        "fontSize": 20,
                        "user-select": "none",
                    }
                }, 
                "⚪ ABOUT US"
            ),

             html.label(
                {
                    "style": {
                        "backgroundColor": "#FFFFFF00",
                        "fontFamily": "Montserrat",
                        "fontWeight": "100",
                        "color": "#FFFFFF",
                        "fontSize": 20,
                        "user-select": "none",
                    }
                }, 
                "📞 CONTACT US"
            ),
        )
    )

run(Website)