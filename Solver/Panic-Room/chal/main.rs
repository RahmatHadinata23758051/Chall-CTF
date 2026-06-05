use std::panic;
use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Usage: ./panic_room <flag>");
        return;
    }
    let input = args[1].as_bytes();
    if input.len() != 30 {
        println!("Goblok! Panjangnya aja salah. AI lu nggak ngasih tau?");
        process::exit(1);
    }

    let mut state: u8 = 0;
    
    // Disable default panic hook to keep it quiet
    panic::set_hook(Box::new(|_| {}));

	let r = panic::catch_unwind(|| {
	    if (input[0] ^ 164) == 205 {
	        panic!("next");
	    }
	});
	if r.is_err() {
	    let r = panic::catch_unwind(|| {
	        if (input[1] ^ 29) == 120 {
	            panic!("next");
	        }
	    });
	    if r.is_err() {
	        let r = panic::catch_unwind(|| {
	            if (input[2] ^ 7) == 115 {
	                panic!("next");
	            }
	        });
	        if r.is_err() {
	            let r = panic::catch_unwind(|| {
	                if (input[3] ^ 190) == 197 {
	                    panic!("next");
	                }
	            });
	            if r.is_err() {
	                let r = panic::catch_unwind(|| {
	                    if (input[4] ^ 71) == 55 {
	                        panic!("next");
	                    }
	                });
	                if r.is_err() {
	                    let r = panic::catch_unwind(|| {
	                        if (input[5] ^ 63) == 11 {
	                            panic!("next");
	                        }
	                    });
	                    if r.is_err() {
	                        let r = panic::catch_unwind(|| {
	                            if (input[6] ^ 58) == 84 {
	                                panic!("next");
	                            }
	                        });
	                        if r.is_err() {
	                            let r = panic::catch_unwind(|| {
	                                if (input[7] ^ 36) == 21 {
	                                    panic!("next");
	                                }
	                            });
	                            if r.is_err() {
	                                let r = panic::catch_unwind(|| {
	                                    if (input[8] ^ 189) == 222 {
	                                        panic!("next");
	                                    }
	                                });
	                                if r.is_err() {
	                                    let r = panic::catch_unwind(|| {
	                                        if (input[9] ^ 27) == 68 {
	                                            panic!("next");
	                                        }
	                                    });
	                                    if r.is_err() {
	                                        let r = panic::catch_unwind(|| {
	                                            if (input[10] ^ 174) == 219 {
	                                                panic!("next");
	                                            }
	                                        });
	                                        if r.is_err() {
	                                            let r = panic::catch_unwind(|| {
	                                                if (input[11] ^ 190) == 208 {
	                                                    panic!("next");
	                                                }
	                                            });
	                                            if r.is_err() {
	                                                let r = panic::catch_unwind(|| {
	                                                    if (input[12] ^ 229) == 146 {
	                                                        panic!("next");
	                                                    }
	                                                });
	                                                if r.is_err() {
	                                                    let r = panic::catch_unwind(|| {
	                                                        if (input[13] ^ 140) == 189 {
	                                                            panic!("next");
	                                                        }
	                                                    });
	                                                    if r.is_err() {
	                                                        let r = panic::catch_unwind(|| {
	                                                            if (input[14] ^ 23) == 121 {
	                                                                panic!("next");
	                                                            }
	                                                        });
	                                                        if r.is_err() {
	                                                            let r = panic::catch_unwind(|| {
	                                                                if (input[15] ^ 152) == 252 {
	                                                                    panic!("next");
	                                                                }
	                                                            });
	                                                            if r.is_err() {
	                                                                let r = panic::catch_unwind(|| {
	                                                                    if (input[16] ^ 109) == 50 {
	                                                                        panic!("next");
	                                                                    }
	                                                                });
	                                                                if r.is_err() {
	                                                                    let r = panic::catch_unwind(|| {
	                                                                        if (input[17] ^ 9) == 56 {
	                                                                            panic!("next");
	                                                                        }
	                                                                    });
	                                                                    if r.is_err() {
	                                                                        let r = panic::catch_unwind(|| {
	                                                                            if (input[18] ^ 8) == 123 {
	                                                                                panic!("next");
	                                                                            }
	                                                                        });
	                                                                        if r.is_err() {
	                                                                            let r = panic::catch_unwind(|| {
	                                                                                if (input[19] ^ 24) == 71 {
	                                                                                    panic!("next");
	                                                                                }
	                                                                            });
	                                                                            if r.is_err() {
	                                                                                let r = panic::catch_unwind(|| {
	                                                                                    if (input[20] ^ 56) == 86 {
	                                                                                        panic!("next");
	                                                                                    }
	                                                                                });
	                                                                                if r.is_err() {
	                                                                                    let r = panic::catch_unwind(|| {
	                                                                                        if (input[21] ^ 60) == 12 {
	                                                                                            panic!("next");
	                                                                                        }
	                                                                                    });
	                                                                                    if r.is_err() {
	                                                                                        let r = panic::catch_unwind(|| {
	                                                                                            if (input[22] ^ 130) == 246 {
	                                                                                                panic!("next");
	                                                                                            }
	                                                                                        });
	                                                                                        if r.is_err() {
	                                                                                            let r = panic::catch_unwind(|| {
	                                                                                                if (input[23] ^ 155) == 196 {
	                                                                                                    panic!("next");
	                                                                                                }
	                                                                                            });
	                                                                                            if r.is_err() {
	                                                                                                let r = panic::catch_unwind(|| {
	                                                                                                    if (input[24] ^ 7) == 51 {
	                                                                                                        panic!("next");
	                                                                                                    }
	                                                                                                });
	                                                                                                if r.is_err() {
	                                                                                                    let r = panic::catch_unwind(|| {
	                                                                                                        if (input[25] ^ 144) == 207 {
	                                                                                                            panic!("next");
	                                                                                                        }
	                                                                                                    });
	                                                                                                    if r.is_err() {
	                                                                                                        let r = panic::catch_unwind(|| {
	                                                                                                            if (input[26] ^ 51) == 81 {
	                                                                                                                panic!("next");
	                                                                                                            }
	                                                                                                        });
	                                                                                                        if r.is_err() {
	                                                                                                            let r = panic::catch_unwind(|| {
	                                                                                                                if (input[27] ^ 184) == 205 {
	                                                                                                                    panic!("next");
	                                                                                                                }
	                                                                                                            });
	                                                                                                            if r.is_err() {
	                                                                                                                let r = panic::catch_unwind(|| {
	                                                                                                                    if (input[28] ^ 167) == 192 {
	                                                                                                                        panic!("next");
	                                                                                                                    }
	                                                                                                                });
	                                                                                                                if r.is_err() {
	                                                                                                                    let r = panic::catch_unwind(|| {
	                                                                                                                        if (input[29] ^ 180) == 201 {
	                                                                                                                            panic!("next");
	                                                                                                                        }
	                                                                                                                    });
	                                                                                                                    if r.is_err() {
	                                                                                                                        println!("Anjay, kok bener? Hoki doang lu pasti.");
	                                                                                                                    } else {
	                                                                                                                        println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                                                        process::exit(1);
	                                                                                                                    }
	                                                                                                                } else {
	                                                                                                                    println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                                                    process::exit(1);
	                                                                                                                }
	                                                                                                            } else {
	                                                                                                                println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                                                process::exit(1);
	                                                                                                            }
	                                                                                                        } else {
	                                                                                                            println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                                            process::exit(1);
	                                                                                                        }
	                                                                                                    } else {
	                                                                                                        println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                                        process::exit(1);
	                                                                                                    }
	                                                                                                } else {
	                                                                                                    println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                                    process::exit(1);
	                                                                                                }
	                                                                                            } else {
	                                                                                                println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                                process::exit(1);
	                                                                                            }
	                                                                                        } else {
	                                                                                            println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                            process::exit(1);
	                                                                                        }
	                                                                                    } else {
	                                                                                        println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                        process::exit(1);
	                                                                                    }
	                                                                                } else {
	                                                                                    println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                    process::exit(1);
	                                                                                }
	                                                                            } else {
	                                                                                println!("Cupu! Balik belajar rev lagi sana.");
	                                                                                process::exit(1);
	                                                                            }
	                                                                        } else {
	                                                                            println!("Cupu! Balik belajar rev lagi sana.");
	                                                                            process::exit(1);
	                                                                        }
	                                                                    } else {
	                                                                        println!("Cupu! Balik belajar rev lagi sana.");
	                                                                        process::exit(1);
	                                                                    }
	                                                                } else {
	                                                                    println!("Cupu! Balik belajar rev lagi sana.");
	                                                                    process::exit(1);
	                                                                }
	                                                            } else {
	                                                                println!("Cupu! Balik belajar rev lagi sana.");
	                                                                process::exit(1);
	                                                            }
	                                                        } else {
	                                                            println!("Cupu! Balik belajar rev lagi sana.");
	                                                            process::exit(1);
	                                                        }
	                                                    } else {
	                                                        println!("Cupu! Balik belajar rev lagi sana.");
	                                                        process::exit(1);
	                                                    }
	                                                } else {
	                                                    println!("Cupu! Balik belajar rev lagi sana.");
	                                                    process::exit(1);
	                                                }
	                                            } else {
	                                                println!("Cupu! Balik belajar rev lagi sana.");
	                                                process::exit(1);
	                                            }
	                                        } else {
	                                            println!("Cupu! Balik belajar rev lagi sana.");
	                                            process::exit(1);
	                                        }
	                                    } else {
	                                        println!("Cupu! Balik belajar rev lagi sana.");
	                                        process::exit(1);
	                                    }
	                                } else {
	                                    println!("Cupu! Balik belajar rev lagi sana.");
	                                    process::exit(1);
	                                }
	                            } else {
	                                println!("Cupu! Balik belajar rev lagi sana.");
	                                process::exit(1);
	                            }
	                        } else {
	                            println!("Cupu! Balik belajar rev lagi sana.");
	                            process::exit(1);
	                        }
	                    } else {
	                        println!("Cupu! Balik belajar rev lagi sana.");
	                        process::exit(1);
	                    }
	                } else {
	                    println!("Cupu! Balik belajar rev lagi sana.");
	                    process::exit(1);
	                }
	            } else {
	                println!("Cupu! Balik belajar rev lagi sana.");
	                process::exit(1);
	            }
	        } else {
	            println!("Cupu! Balik belajar rev lagi sana.");
	            process::exit(1);
	        }
	    } else {
	        println!("Cupu! Balik belajar rev lagi sana.");
	        process::exit(1);
	    }
	} else {
	    println!("Cupu! Balik belajar rev lagi sana.");
	    process::exit(1);
	}
}
