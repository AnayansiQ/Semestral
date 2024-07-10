import prog_1, prog_2, prog_3, prog_4, prog_5
import prog_6, prog_7, prog_8, prog_9, prog_1_if
import prog_2_if, prog_3_if, prog_4_if, prog_5_if, prog_6_if
import prog_7_if, prog_8_if, prog_9_if, prog_10_if, prog_0f
import prog_12_if, prog_13_if, prog_14_if, prog_15_if, prog_16_if
import prog_17_if, prog_18_if, prog_19_if, prog_20_if, prog_1_w
import prog_2_w, prog_3_w, prog_4_w, prog_5_w, prog_6_w
import prog_7_w, prog_8_w, prog_1f, prog_2f, prog_3f
import prog_4f, prog_5f, prog_6f, prog_7f, prog_8f


def main():
    while True:
        print("\n \n                              ↯---[Mis programas python🐍📁]---↯\n")
        print("Ejecutar función de programas:\n  ▶•[1, 9]\n")
        print("Ejecutar función de programas con sentencia if, elif, else:\n ▶•[10,(20 -for) 29]\n")
        print("Ejecutar función de programas con el bucle while:\n ▶•[30, 37]\n")
        print("Ejecutar función de programas con el bucle for:\n ▶•[38,45]\n")
        
        print("|Presiona 0 para salir|\n")
        
        choice = input("Elige el programa que quieres buscar:🔍 ")
        print("\n")

        match choice:
            case "1":
                prog_1.program_1()
            case "2":
                prog_2.program_2()
            case "3":
                prog_3.program_3()
            case "4":
                prog_4.program_4()
            case "5":
                prog_5.program_5()
            case "6":
                prog_6.program_6()
            case "7":
                prog_7.program_7()
            case "8":
                prog_8.program_8()
            case "9":
                prog_9.program_9()
            case "10":
                prog_1_if.program_10()
            case "11":
                prog_2_if.program_11()
            case "12":
                prog_3_if.program_12()
            case "13":
                prog_4_if.program_13()
            case "14":
                prog_5_if.program_14()
            case "15":
                prog_6_if.program_15()
            case "16":
                prog_7_if.program_16()
            case "17":
                prog_8_if.program_17()
            case "18":
                prog_9_if.program_18()
            case "19":
                prog_10_if.program_19()
            case "20":
                prog_0f.program_20()
            case "21":
                prog_12_if.program_21()
            case "22":
                prog_13_if.program_22()
            case "23":
                prog_14_if.program_23()
            case "24":
                prog_15_if.program_24()
            case "25":
                prog_16_if.program_25()
            case "26":
                prog_17_if.program_26()
            case "27":
                prog_18_if.program_27()
            case "28":
                prog_19_if.program_28()
            case "29":
                prog_20_if.program_29()
            case "30":
                prog_1_w.program_30()
            case "31":
                prog_2_w.program_31()
            case "32":
                prog_3_w.program_32()
            case "33":
                prog_4_w.program_33()
            case "34":
                prog_5_w.program_34()
            case "35":
                prog_6_w.program_35()
            case "36":
                prog_7_w.program_36()
            case "37":
                prog_8_w.program_37()
            case "38":
                prog_1f.program_38()
            case "39":
                prog_2f.program_39()
            case "40":
                prog_3f.program_40()
            case "41":
                prog_4f.program_41()
            case "42":
                prog_5f.program_42()
            case "43":
                prog_6f.program_43()
            case "44":
                prog_7f.program_44()
            case "45":
                prog_8f.program_45()
            case "0":
                print("Saliendo del archivero...🚩")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")
                

if __name__ == "__main__":
    main()