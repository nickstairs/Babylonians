b0nano 2.9.3            �   nickstairs                              LAPTOP-OI4N4LMM                         /home/nickstairs/Babylonians/decay.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          init = float(input("Initial Amount: "))
halflife = float(input("Half-Life: "))
time = float(input("Elapsed Time: "))
residual = init*0.5**(time/halflife)
print ("Residual amount remaining =",residual)
print("Finishd")
