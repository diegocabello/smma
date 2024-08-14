back_arrow = r'//*[@id="aD46E48D7-17A1-4194-8C40-79DC4683CC94--32"]/div/div[1]/div/div/div/div[2]/audience-picker/picker/div/div/div/div/dynamic-component/picker-section/div/div[1]/div[1]/div/dynamic-component/section-header/div/material-icon/i'

categories = {
    "Who they are": {
        "selector": r'//*[@id="aD46E48D7-17A1-4194-8C40-79DC4683CC94--32"]/div/div[1]/div/div/div/div[2]/audience-picker/picker/div/div/div/div/dynamic-component/picker-section/div/div/div/div/div/category-group-renderer/category-renderer[1]',
        "data": {
            "parental status": {
                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--30"]/tree-list/div/div',
                "children": {
                    "parents": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--36"]/tree-list[1]/div/div',
                        "children": {
                            "infants": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--36"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "toddlers": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--36"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "preschoolers": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--36"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "grade schoolers": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--36"]/tree-list[4]/div/div',
                                "selected": False
                            },
                            "teens": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--36"]/tree-list[5]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            },
            "marital status": {
                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--32"]/tree-list[1]/div/div',
                "children": {
                    "single": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--32"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "in a relationship": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--32"]/tree-list[2]/div/div',
                        "selected": False
                    },
                    "married": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--32"]/tree-list[3]/div/div',
                        "selected": False
                    }
                }
            },
            "education": {
                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--33"]/tree-list[1]/div/div',
                "children": {
                    "current college students": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--33"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "highest level of educational attainment": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--46"]/tree-list[1]/div/div',
                        "children": {
                            "high school graduate": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--46"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "bachelor's degree": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--46"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "advanced degree": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--46"]/tree-list[3]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            },
            "homeownership status": {
                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--34"]/tree-list[1]/div/div',
                "children": {
                    "homeowners": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--34"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "renters": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--34"]/tree-list[2]/div/div',
                        "selected": False
                    }
                }
            },
            "employment": {
                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--35"]/tree-list[1]/div/div',
                "children": {
                    "company size": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--52"]/tree-list[1]/div/div',
                        "children": {
                            "small employer (1-249 employees)": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--52"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "large employer (250-10k employees)": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--52"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "very large employer (10k+ employees)": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--52"]/tree-list[3]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "industry": {
                        "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[1]/div/div',
                        "children": {
                            "construction industry": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "education sector": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "financial industry": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "healthcare industry": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[4]/div/div',
                                "selected": False
                            },
                            "hospitality industry": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[5]/div/div',
                                "selected": False
                            },
                            "manufacturing industry": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[6]/div/div',
                                "selected": False
                            },
                            "real estate industry": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[7]/div/div',
                                "selected": False
                            },
                            "technology industry": {
                                "selector": r'//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--53"]/tree-list[8]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            }
        }
    },
    "what their interests and habits are": {
        "selector": '//*[@id="aD46E48D7-17A1-4194-8C40-79DC4683CC94--32"]/div/div[1]/div/div/div/div[2]/audience-picker/picker/div/div/div/div/dynamic-component/picker-section/div/div/div/div/div/category-group-renderer/category-renderer[2]/div',
        "selected": False,
        "children": {
            "banking & finance": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--65"]/div/div',
                "selected": False,
                "children": {
                    "avid investors": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--66"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "banks online": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--66"]/tree-list[2]/div/div',
                        "selected": False
                    }
                }
            },
            "beauty & wellness": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--67"]/div/div',
                "selected": False,
                "children": {
                    "beauty mavens": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--67"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "frequently visits salons": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--67"]/tree-list[2]/div/div',
                        "selected": False
                    }
                }
            },
            "food & dining": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--68"]/div/div',
                "selected": False,
                "children": {
                    "coffee shop regulars": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--68"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "cooking enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--108"]/div/div',
                        "selected": False,
                        "children": {
                            "30 minute chefs": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--108"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "aspiring chefs": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--108"]/tree-list[2]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "fast food cravers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--68"]/tree-list[3]/div/div',
                        "selected": False
                    },
                    "foodies": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--68"]/tree-list[4]/div/div',
                        "selected": False
                    },
                    "frequently dines out": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--68"]/tree-list[5]/div/div',
                        "selected": False
                    },
                    "prefers organic food": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--68"]/tree-list[6]/div/div',
                        "selected": False
                    },
                    "vegetarians & vegans": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--113"]/div/div',
                        "selected": True,
                        "children": {
                            "vegans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--113"]/tree-list[1]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            },
            "home & garden": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--69"]/div/div',
                "selected": False,
                "children": {
                    "do-it-yourselfers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--69"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "home decor enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--69"]/tree-list[2]/div/div',
                        "selected": False
                    }
                }
            },
            "lifestyles & hobbies": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/div/div',
                "selected": False,
                "children": {
                    "art & theater aficionados": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "business professionals": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[2]/div/div',
                        "selected": False
                    },
                    "charitable donors & volunteers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[3]/div/div',
                        "selected": False
                    },
                    "family-focused": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--122"]/div/div',
                        "selected": False,
                        "children": {
                            "homeschooling parents": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--122"]/tree-list[1]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "fashionistas": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[5]/div/div',
                        "selected": False
                    },
                    "frequently attends live events": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[6]/div/div',
                        "selected": False
                    },
                    "green living enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[7]/div/div',
                        "selected": False
                    },
                    "nightlife enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[8]/div/div',
                        "selected": False
                    },
                    "outdoor enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[9]/div/div',
                        "selected": False
                    },
                    "pet lovers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--128"]/div/div',
                        "selected": False,
                        "children": {
                            "cat lovers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--128"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "dog lovers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--128"]/tree-list[2]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "shutterbugs": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[11]/div/div',
                        "selected": False
                    },
                    "thrill seekers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--70"]/tree-list[12]/div/div',
                        "selected": False
                    }
                }
            },
            "media & entertainment": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--71"]/div/div',
                "selected": False,
                "children": {
                    "book lovers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--71"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "comics & animation fans": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--71"]/tree-list[2]/div/div',
                        "selected": False
                    },
                    "gamers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/div/div',
                        "selected": False,
                        "children": {
                            "action game fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "adventure & strategy game fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "casual & social gamers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "console gamers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[4]/div/div',
                                "selected": False
                            },
                            "driving & racing game fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[5]/div/div',
                                "selected": False
                            },
                            "esports fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[6]/div/div',
                                "selected": False
                            },
                            "fans of new & upcoming video games": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[7]/div/div',
                                "selected": False
                            },
                            "hardcore gamers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[8]/div/div',
                                "selected": False
                            },
                            "pc gamers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[9]/div/div',
                                "selected": False
                            },
                            "roleplaying game fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[10]/div/div',
                                "selected": False
                            },
                            "shooter game fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[11]/div/div',
                                "selected": False
                            },
                            "sports game fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--80"]/tree-list[12]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "light tv viewers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--71"]/tree-list[4]/div/div',
                        "selected": False
                    },
                    "movie lovers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/div/div',
                        "selected": False,
                        "children": {
                            "action & adventure movie fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "comedy movie fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "family movie fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "fans of new & upcoming movies": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/tree-list[4]/div/div',
                                "selected": False
                            },
                            "fans of south asian film": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/tree-list[5]/div/div',
                                "selected": False
                            },
                            "horror movie fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/tree-list[6]/div/div',
                                "selected": False
                            },
                            "romance & drama movie fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/tree-list[7]/div/div',
                                "selected": False
                            },
                            "sci-fi & fantasy movie fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--82"]/tree-list[8]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "music lovers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/div/div',
                        "selected": False,
                        "children": {
                            "blues fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "classical music enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "country music fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "electronic dance music fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[4]/div/div',
                                "selected": False
                            },
                            "fans of latin music": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[5]/div/div',
                                "selected": False
                            },
                            "folk & traditional music enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[6]/div/div',
                                "selected": False
                            },
                            "indie & alternative rock fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[7]/div/div',
                                "selected": False
                            },
                            "jazz enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[8]/div/div',
                                "selected": False
                            },
                            "metalheads": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[9]/div/div',
                                "selected": False
                            },
                            "pop music fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[10]/div/div',
                                "selected": False
                            },
                            "rap & hip hop fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[11]/div/div',
                                "selected": False
                            },
                            "rock music fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[12]/div/div',
                                "selected": False
                            },
                            "world music fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--83"]/tree-list[13]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "tv lovers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--84"]/div/div',
                        "selected": False,
                        "children": {
                            "documentary & nonfiction tv fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--84"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "family television fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--84"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "game, reality, & talk show fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--84"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "sci-fi & fantasy tv fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--84"]/tree-list[4]/div/div',
                                "selected": False
                            },
                            "tv comedy fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--84"]/tree-list[5]/div/div',
                                "selected": False
                            },
                            "tv drama fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--84"]/tree-list[6]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            },
            "news & politics": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--72"]/div/div',
                "selected": False,
                "children": {
                    "avid news readers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--161"]/div/div',
                        "selected": False,
                        "children": {
                            "avid business news readers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--161"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "avid local news readers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--161"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "avid political news readers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--161"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "avid world news readers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--161"]/tree-list[4]/div/div',
                                "selected": False
                            },
                            "entertainment news enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--161"]/tree-list[5]/div/div',
                                "selected": False
                            },
                            "men's media fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--161"]/tree-list[6]/div/div',
                                "selected": False
                            },
                            "women's media fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--161"]/tree-list[7]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            },
            "shoppers": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--73"]/div/div',
                "selected": False,
                "children": {
                    "bargain hunters": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--73"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "luxury shoppers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--73"]/tree-list[2]/div/div',
                        "selected": False
                    },
                    "shopping enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--73"]/tree-list[3]/div/div',
                        "selected": False
                    },
                    "value shoppers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--73"]/tree-list[4]/div/div',
                        "selected": False
                    }
                }
            },
            "sports & fitness": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--74"]/div/div',
                "selected": False,
                "children": {
                    "health & fitness buffs": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--173"]/div/div',
                        "selected": False,
                        "children": {
                            "weightlifters": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--173"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "yoga lovers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--173"]/tree-list[2]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "sports fans": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/div/div',
                        "selected": False,
                        "children": {
                            "baseball fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "basketball fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "boating & sailing enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "cricket enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[4]/div/div',
                                "selected": False
                            },
                            "cycling enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[5]/div/div',
                                "selected": False
                            },
                            "fans of american football": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[6]/div/div',
                                "selected": False
                            },
                            "fans of australian football": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[7]/div/div',
                                "selected": False
                            },
                            "fight & wrestling fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[8]/div/div',
                                "selected": False
                            },
                            "golf enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[9]/div/div',
                                "selected": False
                            },
                            "hockey fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[10]/div/div',
                                "selected": False
                            },
                            "motor sports enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[11]/div/div',
                                "selected": False
                            },
                            "racquetball enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[12]/div/div',
                                "selected": False
                            },
                            "rugby enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[13]/div/div',
                                "selected": False
                            },
                            "running enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[14]/div/div',
                                "selected": False
                            },
                            "skiing enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[15]/div/div',
                                "selected": False
                            },
                            "soccer fans": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[16]/div/div',
                                "selected": False
                            },
                            "swimming enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[17]/div/div',
                                "selected": False
                            },
                            "tennis enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[18]/div/div',
                                "selected": False
                            },
                            "water sports enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[19]/div/div',
                                "selected": False
                            },
                            "winter sports enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--174"]/tree-list[20]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            },
            "technology": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--75"]/div/div',
                "selected": False,
                "children": {
                    "mobile enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--75"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "social media enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--75"]/tree-list[2]/div/div',
                        "selected": False
                    },
                    "technophiles": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--199"]/div/div',
                        "selected": False,
                        "children": {
                            "audiophiles": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--199"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "cloud services power users": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--199"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "high-end computer aficionados": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--199"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "home automation enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--199"]/tree-list[4]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            },
            "travel": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--76"]/div/div',
                "selected": False,
                "children": {
                    "business travelers": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--76"]/tree-list[1]/div/div',
                        "selected": False
                    },
                    "travel buffs": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--205"]/div/div',
                        "selected": False,
                        "children": {
                            "beachbound travelers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--205"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "family vacationers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--205"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "luxury travelers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--205"]/tree-list[3]/div/div',
                                "selected": False
                            },
                            "snowbound travelers": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--205"]/tree-list[4]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            },
            "vehicles & transportation": {
                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--77"]/div/div',
                "selected": False,
                "children": {
                    "auto enthusiasts": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--210"]/div/div',
                        "selected": False,
                        "children": {
                            "motorcycle enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--210"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "performance & luxury vehicle enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--210"]/tree-list[2]/div/div',
                                "selected": False
                            },
                            "truck & suv enthusiasts": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--210"]/tree-list[3]/div/div',
                                "selected": False
                            }
                        }
                    },
                    "transportation modes": {
                        "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--211"]/div/div',
                        "selected": False,
                        "children": {
                            "public transit users": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--211"]/tree-list[1]/div/div',
                                "selected": False
                            },
                            "taxi service users": {
                                "selector": '//*[@id="aBA6D2BC9-1CBC-46BB-9577-1004A86B400A--211"]/tree-list[2]/div/div',
                                "selected": False
                            }
                        }
                    }
                }
            }
        }
    },
    'what they are actively researching or marketing': {
            "selector": r'//*[@id="aD46E48D7-17A1-4194-8C40-79DC4683CC94--32"]/div/div[1]/div/div/div/div[2]/audience-picker/picker/div/div/div/div/dynamic-component/picker-section/div/div/div/div/div/category-group-renderer/category-renderer[2]/div',
            "data": {
                'in market': {
                    'Apparel & Accessories': {
                        'active': False,
                        'children': {
                            'Activewear': False,
                            'Athletic Shoes': False,
                            'Boots': False,
                            'Bridal Wear': False,
                            'Costumes': False,
                            'Dress Shoes': False,
                            'Eyewear': False,
                            'Fine Jewelry': False,
                            'Formal Wear': False,
                            'Handbags': False,
                            'Jewelry & Watches': False,
                            'Lingerie': False,
                            'Luggage': False,
                            "Men's Apparel": False,
                            'Necklaces': False,
                            'Outerwear': False,
                            'Running Apparel': False,
                            'Shoes': False,
                            'Socks': False,
                            'Suits & Business Attire': False,
                            'Sunglasses': False,
                            'Swimwear': False,
                            'Underwear': False,
                            'Wallets, Briefcases & Leather Goods': False,
                            'Watches': False,
                            'Wedding & Engagement Rings': False,
                            "Women's Apparel": False,
                            'Yoga Apparel': False
                        }
                    },
                    'Arts & Crafts Supplies': False,
                    'Autos & Vehicles': {
                        'active': False,
                        'children': {
                            'Acura': False,
                            'Alfa Romeo': False,
                            'Audi': False,
                            'Auto Exterior Parts & Accessories': False,
                            'Auto Interior Parts & Accessories': False,
                            'Auto Parts & Accessories': False,
                            'Auto Repair & Maintenance': False,
                            'Automotive Electronic Components': False,
                            'BMW': False,
                            'Bicycles & Accessories': False,
                            'Boats & Watercraft': False,
                            'Brake Service & Repair': False,
                            'Buick': False,
                            'Cadillac': False,
                            'Campers & RVs': False,
                            'Car Batteries': False,
                            'Car Brakes': False,
                            'Chevrolet': False,
                            'Chrysler': False,
                            'Citroën': False,
                            'Classic Vehicles': False,
                            'Collision & Auto Body Repair': False,
                            'Commercial Vehicles': False,
                            'Compact Cars': False,
                            'Compact Cars (New)': False,
                            'Compact Cars (Used)': False,
                            'Convertibles': False,
                            'Convertibles (New)': False,
                            'Convertibles (Used)': False,
                            'Coupes': False, 
                            'Coupes (New)': False,
                            'Coupes (Used)': False,
                            'Crossovers': False,
                            'Crossovers (New)': False,
                            'Crossovers (Used)': False, 
                            'Diesel Vehicles': False,
                            'Diesel Vehicles (New)': False,
                            'Diesel Vehicles (Used)': False, 
                            'Dodge': False, 
                            'Engine & Transmission': False, 
                            'Fiat': False, 
                            'Ford': False, 
                            'GMC': False, 
                            'Glass Repair & Replacement': False, 
                            'Hatchbacks': False, 
                            'Hatchbacks (New)': False,
                            'Hatchbacks (Used)': False,
                            'High Performance & Aftermarket Auto Parts': False, 
                            'Honda': False, 
                            'Hybrid & Alternative Vehicles': False, 
                            'Hybrid & Alternative Vehicles (New)': False,
                            'Hybrid & Alternative Vehicles (Used)': False,
                            'Hyundai': False, 
                            'Infiniti': False, 
                            'Isuzu': False, 
                            'Jaguar': False, 
                            'Jeep': False, 
                            'Kia': False, 
                            'Land Rover': False, 
                            'Lexus': False, 
                            'Lincoln': False, 
                            'Luxury Vehicles': False, 
                            'Luxury Vehicles (New)': False,
                            'Luxury Vehicles (Used)': False,
                            'Maserati': False, 
                            'Mazda': False, 
                            'Mercedes-Benz': False, 
                            'Microcars & Subcompacts': False, 
                            'Microcars & Subcompacts (New)': False,
                            'Microcars & Subcompacts (Used)': False,
                            'Mini': False, 
                            'Mitsubishi': False,
                            'Motor Vehicles': False,
                            'Motor Vehicles (New)': False,
                            'Motor Vehicles (Used)': False, 
                            'Motor Vehicles by Brand': False,
                            'Motor Vehicles by Type': False, 
                            'Motorcycles': False, 
                            'Motorcycles (New)': False,
                            'Motorcycles (Used)': False, 
                            'Nissan': False, 
                            'Off-Road Vehicles': False,
                            'Off-Road Vehicles (New)': False,
                            'Off-Road Vehicles (Used)': False,
                            'Oil Changes': False, 
                            'Peugeot': False, 
                            'Pickup Trucks': False, 
                            'Pickup Trucks (New)': False,
                            'Pickup Trucks (Used)': False,
                            'Porsche': False, 
                            'Ram Trucks': False, 
                            'Renault': False,
                            'SEAT': False, 
                            'SUVs': False, 
                            'SUVs (New)': False,
                            'SUVs (Used)': False, 
                            'Scion': False, 
                            'Scooters & Mopeds': False, 
                            'Scooters & Mopeds (New)': False, 
                            'Scooters & Mopeds (Used)': False, 
                            'Sedans': False, 
                            'Sedans (New)': False, 
                            'Sedans (Used)': False, 
                            'Sports Cars': False, 
                            'Sports Cars (New)': False,
                            'Sports Cars (Used)': False, 
                            'Station Wagons': False,
                            'Station Wagons (New)': False,
                            'Station Wagons (Used)': False, 
                            'Subaru': False, 
                            'Suzuki': False, 
                            'Tesla Motors': False, 
                            'Toyota': False, 
                            'Transmission Repair': False, 
                            'Vans & Minivans': False, 
                            'Vans & Minivans (New)': False, 
                            'Vans & Minivans (Used)': False, 
                            'Vauxhall-Opel': False, 
                            'Vehicles (Other)': False,
                            'Volkswagen': False, 
                            'Volvo': False, 
                            'Wheels & Tires': False 
                        }
                    },
                    "Baby & Children's Products": {
                        'active': False,
                        'children': {
                            'Baby & Children\'s Apparel': False,
                            'Baby & Toddler Apparel': False,
                            'Child Car Seats': False, 
                            'Childcare': False, 
                            'Childcare & Education': False,
                            'Children\'s Apparel': False, 
                            'Diapers & Baby Hygiene Products': False,
                            'Early Childhood Education': False, 
                            'Infant & Toddler Feeding': False,
                            'Infant Feeding Supplies': False, 
                            'Strollers & Baby Carriages': False,
                            'Toddler Meals': False, 
                            'Toys': False
                        }
                    },
                    'Beauty & Personal Care': {
                        'active': False, 
                        'children': {
                            'Bath & Body Products': False, 
                            'Body Lotions & Moisturizers': False, 
                            'Eye Makeup': False, 
                            'Face Lotions & Moisturizers': False, 
                            'Face Makeup': False, 
                            'Facial Cleansers & Makeup Removers': False, 
                            'Hair Care Products': False, 
                            'Hair Color Products': False, 
                            'Lip Makeup': False, 
                            'Makeup & Cosmetics': False,
                            'Manicures & Pedicures': False, 
                            'Nail Care Products': False,
                            'Perfumes & Fragrances': False, 
                            'Shampoos & Conditioners': False,
                            'Skin Care Products': False, 
                            'Spas & Beauty Services': False, 
                            'Tanning & Sun Care Products': False
                        }
                    }, 
                    'Business & Industrial Products': False,
                    'Business Services': {
                        'active': False, 
                        'children': {
                            'Advertising & Marketing Services': False,
                            'Business Financial Services': False, 
                            'Business Printing & Document Services': False,
                            'Business Technology': False, 
                            'CRM Solutions': False,
                            'Collaboration & Conferencing Tools': False, 
                            'Corporate Event Planning': False,
                            'Domain Registration': False, 
                            'ERP Solutions': False, 
                            'Email Marketing Services': False,
                            'Enterprise Software': False, 
                            'Helpdesk & Customer Support Solutions': False,
                            'Hosted Data & Cloud Storage': False, 
                            'Network & Enterprise Security': False, 
                            'Network Equipment & Virtualization': False, 
                            'Network Management': False, 
                            'Network Systems & Services': False, 
                            'Office Furniture': False, 
                            'Office Supplies': False, 
                            'Payment Processing & Merchant Services': False, 
                            'Payroll Services': False, 
                            'Physical Security & Access Control': False,
                            'SEO & SEM Services': False, 
                            'Staffing & Recruitment Services': False,
                            'Web Design & Development': False, 
                            'Web Hosting': False, 
                            'Web Services': False 
                        }
                    }, 
                    'Computers & Peripherals': {
                        'active': False,
                        'children': {
                            'Computer Accessories & Components': False, 
                            'Computer Monitors': False,
                            'Computers': False, 
                            'Desktop Computers': False, 
                            'Laptops & Notebooks': False, 
                            'Memory & Storage': False,
                            'Printers, Scanners & Faxes': False, 
                            'Tablets & Ultraportable Devices': False
                        }
                    }, 
                    'Consumer Electronics': {
                        'active': False, 
                        'children': {
                            'Android Phones': False, 
                            'Audio': False, 
                            'Camcorders': False, 
                            'Camera Lenses': False, 
                            'Cameras': False,
                            'Car Audio': False, 
                            'Digital SLRs': False, 
                            'Game Consoles': False, 
                            'Gaming Peripherals & Accessories': False, 
                            'Headphones & Headsets': False, 
                            'Home Theater Systems': False,
                            'Mobile Phone Accessories': False, 
                            'Mobile Phones': False, 
                            'Nintendo Consoles': False,
                            'Pro Musician & DJ Equipment': False, 
                            'Sony PlayStation': False, 
                            'Speakers': False, 
                            'Stereo Systems': False, 
                            'Televisions': False,
                            'Xbox': False, 
                            'iOS Phones': False
                        }
                    }, 
                    'Dating Services': False, 
                    'Education': {
                        'active': False,
                        'children': {
                            'Arts & Design Education': False, 
                            'Business Education': False, 
                            'Cosmetology Education & Training': False, 
                            'Educational Resources (Preschool & Kindergarten)': False, 
                            'Educational Resources (Primary School)': False,
                            'Educational Resources (Secondary School)': False, 
                            'Foreign Language Study': False,
                            'Health Care Education': False, 
                            'Nursing Education': False, 
                            'Open Online Courses': False, 
                            'Post-Secondary Education': False, 
                            'Primary & Secondary Schools (K-12)': False, 
                            'Study Abroad Programs': False,
                            'Technology Education': False, 
                            'Test Preparation & Tutoring': False
                        }
                    },
                    'Employment': {
                        'active': False, 
                        'children': {
                            'Accounting & Finance Jobs': False, 
                            'Agriculture Jobs': False,
                            'Career Consulting Services': False, 
                            'Clerical & Administrative Jobs': False, 
                            'Construction Jobs': False, 
                            'Education Jobs': False, 
                            'Executive & Management Jobs': False, 
                            'Government & Public Sector Jobs': False,
                            'Health & Medical Jobs': False,
                            'IT & Technical Jobs': False, 
                            'Internships': False, 
                            'Legal Jobs': False, 
                            'Leisure & Hospitality Jobs': False,
                            'Manufacturing Jobs': False,
                            'Resumes & Portfolios': False,
                            'Retail Jobs': False, 
                            'Sales & Marketing Jobs': False, 
                            'Temporary & Seasonal Jobs': False, 
                            'Transportation & Utilities Jobs': False
                        }
                    },
                    'Event Tickets': {
                        'active': False, 
                        'children': {
                            'American Football Tickets': False,
                            'Baseball Tickets': False, 
                            'Basketball Tickets': False,
                            'Broadway & Theater Tickets': False, 
                            'Concert & Music Festival Tickets': False,
                            'Hockey Tickets': False, 
                            'Performing Arts Tickets': False,
                            'Soccer Tickets': False, 
                            'Sports Tickets': False 
                        }
                    },
                    'Financial Services': {
                        'active': False, 
                        'children': {
                            'Auto Insurance': False, 
                            'Auto Loans': False, 
                            'Banking Services': False, 
                            'Business Loans': False,
                            'Credit & Lending': False, 
                            'Credit Cards': False,
                            'Credit Reports & Monitoring Services': False, 
                            'Debit & Checking Services': False, 
                            'Estate Planning': False, 
                            'Financial Planning': False, 
                            'Health Insurance': False,
                            'Home Equity Loans': False, 
                            'Home Insurance': False, 
                            'Home Purchase Loans': False, 
                            'Insurance': False, 
                            'Investment Services': False,
                            'Life Insurance': False, 
                            'Mortgage': False, 
                            'Mortgage Refinancing': False,
                            'Personal Loans': False, 
                            'Retirement Planning': False, 
                            'Savings Accounts': False,
                            'Student Loans': False, 
                            'Tax Preparation Services & Software': False, 
                            'Travel Insurance': False 
                        }
                    }, 
                    'Food': {
                        'active': False, 
                        'children': {
                            'Baked Goods': False,
                            'Candy & Chocolate': False,
                            'Dairy & Eggs': False, 
                            'Fast Food Meals': False, 
                            'Grocery Delivery': False, 
                            'Pizza': False,
                            'Restaurant Delivery & Takeout': False 
                        }
                    },
                    'Gifts & Occasions': {
                        'active': False, 
                        'children': {
                            'Christmas Items & Decor': False, 
                            'Event Photographers & Studios': False, 
                            'Event Planning Services': False, 
                            'Flowers': False, 
                            'Gift Baskets': False,
                            'Halloween Items & Decor': False, 
                            'Holiday Items & Decorations': False, 
                            'Party Supplies': False, 
                            'Party Supplies & Planning': False,
                            'Personalized Gifts': False,
                            'Photo & Video Services': False, 
                            'Photo Printing Services': False, 
                            'Valentine\'s Day Items & Decor': False, 
                            'Wedding Planning': False
                        }
                    },
                    'Home & Garden': {
                        'active': False, 
                        'children': {
                            'Architectural Services': False, 
                            'BBQs & Grills': False, 
                            'Bedding': False, 
                            'Bedroom': False,
                            'Beds & Bed Frames': False, 
                            'Carpet Installation': False, 
                            'Ceiling Light Fixtures': False, 
                            'Climate Control & Air Quality': False, 
                            'Coffee & Espresso Makers': False, 
                            'Cooking Ranges & Stoves': False, 
                            'Cookware & Bakeware': False,
                            'Curtains & Window Treatments': False,
                            'Desks': False, 
                            'Dishwashers': False, 
                            'Door & Window Installation': False, 
                            'Electrician Services': False,
                            'Fine Art': False, 
                            'Fireplaces': False, 
                            'Flooring': False, 
                            'Flooring Services': False, 
                            'Garden & Outdoor Furniture': False, 
                            'Garden Sheds & Outdoor Structures': False, 
                            'General Contracting & Remodeling Services': False,
                            'Hand Sanitizers': False, 
                            'Home & Garden Services': False, 
                            'Home Appliances': False, 
                            'Home Cleaning Services': False,
                            'Home Decor': False,
                            'Home Furnishings': False, 
                            'Home Improvement': False, 
                            'Home Inspection Services': False, 
                            'Home Office': False, 
                            'Home Security': False,
                            'Home Storage & Shelving': False, 
                            'Household Cleaning Supplies': False,
                            'Household Supplies': False, 
                            'Interior Design & Decorating Services': False, 
                            'Juicers & Blenders': False, 
                            'Kitchen & Bathroom Cabinets': False, 
                            'Kitchen & Bathroom Counters': False, 
                            'Kitchen & Dining Room': False, 
                            'Kitchen & Dining Room Tables': False,
                            'Kitchen Appliance Accessories': False,
                            'Landscape Design': False, 
                            'Lawn & Garden Maintenance': False,
                            'Lawn Care & Gardening Supplies': False, 
                            'Lawn Mowers': False, 
                            'Lights & Fixtures': False, 
                            'Living Room': False, 
                            'Locksmith Services': False, 
                            'Mattresses': False, 
                            'Microwaves': False, 
                            'Mixers': False,
                            'Moving & Relocation': False,
                            'New Apartments (For Sale)': False, 
                            'New Houses (For Sale)': False,
                            'Nursery': False, 
                            'Outdoor Furniture Sets': False,
                            'Outdoor Items': False, 
                            'Paint': False, 
                            'Painting Services': False,
                            'Pest Control Services': False,
                            'Pet Supplies': False,
                            'Plumbing Fixture Hardware & Parts': False, 
                            'Plumbing Fixtures': False,
                            'Plumbing Services': False, 
                            'Pools & Spas': False, 
                            'Power & Electrical Supplies': False, 
                            'Preowned Apartments (For Sale)': False, 
                            'Preowned Houses (For Sale)': False, 
                            'Refrigerators': False, 
                            'Residential Properties': False,
                            'Residential Properties (For Rent)': False,
                            'Residential Properties (For Sale)': False, 
                            'Roofing Services': False, 
                            'Rugs & Carpets': False, 
                            'Small Appliances': False, 
                            'Tableware': False, 
                            'Tools': False,
                            'Unfurnished Apartments': False, 
                            'Vacuums': False, 
                            'Washers & Dryers': False,
                            'Water Purifiers': False 
                        }
                    }, 
                    'Media & Entertainment': {
                        'active': False,
                        'children': {
                            'Audio Streaming Subscription Services': False, 
                            'Board Games': False, 
                            'Books': False,
                            'DVDs & Videos': False,
                            'TV & Video Streaming Subscription Services': False, 
                            'Video Game Streaming Services': False, 
                            'Video Games': False 
                        }
                    },
                    'Musical Instruments & Accessories': False, 
                    'Real Estate': {
                        'active': False, 
                        'children': {
                            'Apartments (For Rent)': False,
                            'Apartments (For Sale)': False, 
                            'Commercial Properties': False, 
                            'Commercial Properties (For Rent)': False,
                            'Commercial Properties (For Sale)': False, 
                            'Furnished Apartments': False, 
                            'Houses (For Rent)': False, 
                            'Houses (For Sale)': False,
                            'Moving & Relocation': False,
                            'New Apartments (For Sale)': False, 
                            'New Houses (For Sale)': False, 
                            'Preowned Apartments (For Sale)': False,
                            'Preowned Houses (For Sale)': False, 
                            'Residential Properties': False, 
                            'Residential Properties (For Rent)': False,
                            'Residential Properties (For Sale)': False, 
                            'Unfurnished Apartments': False 
                        }
                    }, 
                    'Seasonal Shopping': {
                        'active': False, 
                        'children': {
                            'After-Christmas Sale Shopping': False,
                            'Back-to-School Apparel & Accessories': False, 
                            'Back-to-School Shopping': False, 
                            'Black Friday Shopping': False, 
                            'Christmas Shopping': False,
                            'In-Store Black Friday Shopping': False, 
                            'In-Store Christmas Shopping': False,
                            'Mother\'s Day Dining': False,
                            'Mother\'s Day Flowers & Greeting Cards': False, 
                            'Mother\'s Day Shopping': False, 
                            'Online Black Friday Shopping': False, 
                            'Online Christmas Shopping': False, 
                            'School Supplies': False 
                        }
                    },
                    'Software': {
                        'active': False, 
                        'children': {
                            'Accounting Software': False, 
                            'Antivirus & Security Software': False,
                            'Audio & Music Software': False, 
                            'Business & Productivity Software': False,
                            'Design Software': False, 
                            'Drawing & Animation Software': False, 
                            'Photo Software': False,
                            'Video Chat Software': False,
                            'Video Editing & Production Software': False 
                        }
                    },
                    'Sports & Fitness': {
                        'active': False,
                        'children': {
                            'Baseball Equipment': False, 
                            'Camping & Hiking Equipment': False, 
                            'Cardio Training Equipment': False,
                            'Exercise Equipment': False, 
                            'Fishing Equipment': False, 
                            'Fitness Classes & Personal Training Services': False, 
                            'Fitness Products & Services': False, 
                            'Fitness Technology Products': False, 
                            'Golf Equipment': False, 
                            'Gyms & Athletic Clubs': False,
                            'Hockey Equipment': False, 
                            'Online Fitness Classes': False, 
                            'Outdoor Recreational Equipment': False, 
                            'Skateboarding Equipment': False, 
                            'Soccer Equipment': False, 
                            'Sporting Goods': False, 
                            'Water Activities Equipment & Accessories': False, 
                            'Weights & Strength Training Equipment': False, 
                            'Winter Sports Equipment & Accessories': False 
                        }
                    },
                    'Telecom': {
                        'active': False,
                        'children': {
                            'Cable & Satellite TV Providers': False,
                            'Internet Service Providers': False,
                            'Mobile Phone Service Providers': False
                        }
                    },
                    'Travel': {
                        'active': False, 
                        'children': {
                            '1 & 2 Star Hotels': False,
                            '3 Star Hotels': False,
                            '4 Star Hotels': False,
                            '5 Star Hotels': False, 
                            'Air Travel': False, 
                            'Air Travel by Class': False, 
                            'Bus & Rail Travel': False,
                            'Business & First Class': False,
                            'Car Rental': False, 
                            'Cruises': False, 
                            'Economy Class': False, 
                            'Economy, Compact & Mid-size Car Rental': False,
                            'Full-size & Standard Car Rental': False,
                            'Hotels & Accommodations': False, 
                            'Hotels by Star Rating': False, 
                            'Luxury, Convertible & Specialty Car Rental': False, 
                            'Minivan & SUV Rental': False,
                            'Trips by Destination': False,
                            'Trips to Abu Dhabi': False,
                            'Trips to Acapulco': False, 
                            'Trips to Ahmedabad': False, 
                            'Trips to Alaska': False,
                            'Trips to Alicante': False, 
                            'Trips to Amsterdam': False, 
                            'Trips to Ankara': False,
                            'Trips to Antalya': False, 
                            'Trips to Asia-Pacific': False, 
                            'Trips to Atlanta': False,
                            'Trips to Atlantic City': False, 
                            'Trips to Austin': False,
                            'Trips to Australia': False,
                            'Trips to Bali': False, 
                            'Trips to Baltimore': False, 
                            'Trips to Bandung': False, 
                            'Trips to Bangkok': False, 
                            'Trips to Barcelona': False,
                            'Trips to Beijing': False,
                            'Trips to Berlin': False, 
                            'Trips to Bilbao': False, 
                            'Trips to Birmingham, AL': False, 
                            'Trips to Birmingham, UK': False,
                            'Trips to Bogota': False, 
                            'Trips to Bologna': False, 
                            'Trips to Bordeaux': False, 
                            'Trips to Boston': False,
                            'Trips to Brazil': False, 
                            'Trips to Brisbane': False,
                            'Trips to Brussels': False, 
                            'Trips to Budapest': False,
                            'Trips to Buffalo-Rochester Area': False, 
                            'Trips to Calgary': False,
                            'Trips to California': False, 
                            'Trips to Canada': False, 
                            'Trips to Cancun & Playa del Carmen': False,
                            'Trips to Cape Town': False, 
                            'Trips to Charleston, SC': False, 
                            'Trips to Charlotte': False,
                            'Trips to Chengdu': False, 
                            'Trips to Chennai': False, 
                            'Trips to Chiang Mai': False,
                            'Trips to Chicago': False, 
                            'Trips to China': False,
                            'Trips to Cincinnati': False, 
                            'Trips to Cleveland': False,
                            'Trips to Cologne': False, 
                            'Trips to Columbus': False,
                            'Trips to Copenhagen': False, 
                            'Trips to Cordoba': False, 
                            'Trips to Costa Rica': False,
                            'Trips to Croatia': False,
                            'Trips to Cuba': False,
                            'Trips to Dallas-Fort Worth': False,
                            'Trips to Delhi': False,
                            'Trips to Denmark': False,
                            'Trips to Denver': False,
                            'Trips to Detroit': False,
                            'Trips to Doha': False,
                            'Trips to Dubai': False,
                            'Trips to Dublin': False,
                            'Trips to Dusseldorf': False,
                            'Trips to Edinburgh': False,
                            'Trips to Egypt': False,
                            'Trips to Europe': False,
                            'Trips to Faro': False,
                            'Trips to Florence': False,
                            'Trips to Florida': False,
                            'Trips to Fort Lauderdale': False,
                            'Trips to Fort Myers': False,
                            'Trips to France': False,
                            'Trips to Frankfurt': False,
                            'Trips to Fukuoka': False,
                            'Trips to Gatlinburg': False,
                            'Trips to Geneva': False,
                            'Trips to Germany': False,
                            'Trips to Glasgow': False,
                            'Trips to Goa': False,
                            'Trips to Granada': False,
                            'Trips to Greece': False,
                            'Trips to Greenville, SC': False,
                            'Trips to Guadalajara': False,
                            'Trips to Guangzhou': False,
                            'Trips to Guatemala': False,
                            'Trips to Hamburg': False,
                            'Trips to Hanoi': False,
                            'Trips to Hartford': False,
                            'Trips to Hawaii': False,
                            'Trips to Helsinki': False,
                            'Trips to Ho Chi Minh City': False,
                            'Trips to Hong Kong': False,
                            'Trips to Houston': False,
                            'Trips to Hungary': False,
                            'Trips to Hyderabad': False,
                            'Trips to Iceland': False,
                            'Trips to India': False,
                            'Trips to Indianapolis': False,
                            'Trips to Indonesia': False,
                            'Trips to Ireland': False,
                            'Trips to Israel': False,
                            'Trips to Istanbul': False,
                            'Trips to Italy': False,
                            'Trips to Izmir': False,
                            'Trips to Jacksonville': False,
                            'Trips to Jamaica': False,
                            'Trips to Japan': False,
                            'Trips to Jeddah': False,
                            'Trips to Johannesburg': False,
                            'Trips to Jordan': False,
                            'Trips to Kansas City': False,
                            'Trips to Kenya': False,
                            'Trips to Key West': False,
                            'Trips to Kiev': False,
                            'Trips to Kochi (India)': False,
                            'Trips to Kolkata': False,
                            'Trips to Krakow': False,
                            'Trips to Kuala Lumpur': False,
                            'Trips to Kuwait': False,
                            'Trips to Kyoto-Osaka-Kobe': False,
                            'Trips to Las Vegas': False,
                            'Trips to Latin America': False,
                            'Trips to Lebanon': False,
                            'Trips to Lima': False,
                            'Trips to Lisbon': False,
                            'Trips to Little Rock': False,
                            'Trips to London, UK': False,
                            'Trips to Los Angeles': False,
                            'Trips to Los Cabos': False,
                            'Trips to Louisville': False,
                            'Trips to Lyon': False,
                            'Trips to Madrid': False,
                            'Trips to Malaga': False,
                            'Trips to Malaysia': False,
                            'Trips to Mallorca, Ibiza & Balearic Islands': False,
                            'Trips to Malta': False,
                            'Trips to Manchester, UK': False,
                            'Trips to Marseille': False,
                            'Trips to Maui': False,
                            'Trips to Melbourne': False,
                            'Trips to Memphis': False,
                            'Trips to Mexico': False,
                            'Trips to Mexico City': False,
                            'Trips to Miami': False,
                            'Trips to Milan': False,
                            'Trips to Milwaukee': False,
                            'Trips to Minneapolis-Saint Paul': False,
                            'Trips to Monterrey': False,
                            'Trips to Montreal': False,
                            'Trips to Morocco': False,
                            'Trips to Moscow': False,
                            'Trips to Mumbai': False,
                            'Trips to Munich': False,
                            'Trips to Myrtle Beach & Grand Strand': False,
                            'Trips to Nagoya': False,
                            'Trips to Nassau': False,
                            'Trips to Nashville': False,
                            'Trips to Nepal': False,
                            'Trips to New Orleans': False,
                            'Trips to New York City': False,
                            'Trips to New Zealand': False,
                            'Trips to Nice': False,
                            'Trips to Norfolk-Virginia Beach Region': False,
                            'Trips to North America': False,
                            'Trips to Oahu': False,
                            'Trips to Ocean City, MD': False,
                            'Trips to Okinawa': False,
                            'Trips to Oklahoma City': False,
                            'Trips to Omaha': False,
                            'Trips to Orange County, CA': False,
                            'Trips to Orlando': False,
                            'Trips to Oslo': False,
                            'Trips to Ottawa': False,
                            'Trips to Panama': False,
                            'Trips to Paris': False,
                            'Trips to Penang': False,
                            'Trips to Pensacola': False,
                            'Trips to Perth': False,
                            'Trips to Philadelphia': False,
                            'Trips to Phoenix': False,
                            'Trips to Pittsburgh': False,
                            'Trips to Poland': False,
                            'Trips to Portland, OR': False,
                            'Trips to Porto': False,
                            'Trips to Portugal': False,
                            'Trips to Prague': False,
                            'Trips to Puerto Rico': False,
                            'Trips to Puerto Vallarta': False,
                            'Trips to Pune': False,
                            'Trips to Raleigh-Durham Area': False,
                            'Trips to Reno': False,
                            'Trips to Richmond, VA': False,
                            'Trips to Rio de Janeiro': False,
                            'Trips to Riyadh': False,
                            'Trips to Romania': False,
                            'Trips to Rome': False,
                            'Trips to Salt Lake City': False,
                            'Trips to Salvador': False,
                            'Trips to San Antonio': False,
                            'Trips to San Diego': False,
                            'Trips to San Francisco Bay Area': False,
                            'Trips to Santiago': False,
                            'Trips to Sapporo': False,
                            'Trips to Savannah': False,
                            'Trips to Seattle': False,
                            'Trips to Seoul': False,
                            'Trips to Seville': False,
                            'Trips to Shanghai': False,
                            'Trips to Sicily': False,
                            'Trips to Singapore': False,
                            'Trips to Sofia': False,
                            'Trips to South Africa': False,
                            'Trips to Spain': False,
                            'Trips to Sri Lanka': False,
                            'Trips to St. Louis': False,
                            'Trips to St. Petersburg': False,
                            'Trips to Stockholm': False,
                            'Trips to Stuttgart': False,
                            'Trips to Sweden': False,
                            'Trips to Switzerland': False,
                            'Trips to Sydney': False,
                            'Trips to Taipei': False,
                            'Trips to Tampa Bay Area': False,
                            'Trips to Tehran': False,
                            'Trips to Thailand': False,
                            'Trips to the Big Island': False,
                            'Trips to the Canary Islands': False,
                            'Trips to the Caribbean': False,
                            'Trips to the Dominican Republic': False,
                            'Trips to the Middle East & Africa': False,
                            'Trips to the Philippines': False,
                            'Trips to the UK': False,
                            'Trips to the US': False,
                            'Trips to the United Arab Emirates': False,
                            'Trips to Tokyo': False,
                            'Trips to Toronto': False,
                            'Trips to Toulouse': False,
                            'Trips to Tucson': False,
                            'Trips to Turkey': False,
                            'Trips to Valencia': False,
                            'Trips to Vancouver': False,
                            'Trips to Venice': False,
                            'Trips to Vienna': False,
                            'Trips to Vietnam': False,
                            'Trips to Warsaw': False,
                            'Trips to Washington, D.C.': False,
                            'Trips to Zurich': False,
                            'Vacation Rentals': False
                            }
                        }
                    } 
                }
            }
        }
    } 