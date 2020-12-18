def check_best_conditions(T, shirtsL, shirtsM, shirtsS, swimL, swimM, swimS, pantsL, pantsM, pantsS, jacketsL, jacketsM, jacketsS, bootsL, bootsM, bootsS):
    for i in range(5):
        temp = T

        #shirts
        temp.add_constraint(shirtsL[i])
        if(temp.is_satisfiable()):
            T.add_constraint(shirtsL[i])
        else:
            temp.remove_constraint(shirtsL[i])
            temp.add_constraint(shirtsM[i])
            if(temp.is_satisfiable()):
                T.add_constraint(shirtsM[i])
            else:
                temp.remove_constraint(shirtsM[i])
                temp.add_constraint(shirtsS[i])
                if(temp.is_satisfiable()):
                    T.add_constraint(shirtsS[i])
                else:
                    temp.remove_constraint(shirtsS[i])

        #swim
        temp.add_constraint(swimL[i])
        if(temp.is_satisfiable()):
            T.add_constraint(swimL[i])
        else:
            temp.remove_constraint(swimL[i])
            temp.add_constraint(swimM[i])
            if(temp.is_satisfiable()):
                T.add_constraint(swimM[i])
            else:
                temp.remove_constraint(swimM[i])
                temp.add_constraint(swimS[i])
                if(temp.is_satisfiable()):
                    T.add_constraint(swimS[i])
                else:
                    temp.remove_constraint(swimS[i])

        #pants
        temp.add_constraint(pantsL[i])
        if(temp.is_satisfiable()):
            T.add_constraint(pantsL[i])
        else:
            temp.remove_constraint(pantsL[i])
            temp.add_constraint(pantsM[i])
            if(temp.is_satisfiable()):
                T.add_constraint(pantsM[i])
            else:
                temp.remove_constraint(pantsM[i])
                temp.add_constraint(pantsS[i])
                if(temp.is_satisfiable()):
                    T.add_constraint(pantsS[i])
                else:
                    temp.remove_constraint(pantsS[i])

        #jackets
        temp.add_constraint(jacketsL[i])
        if(temp.is_satisfiable()):
            T.add_constraint(jacketsL[i])
        else:
            temp.remove_constraint(jacketsL[i])
            temp.add_constraint(jacketsM[i])
            if(temp.is_satisfiable()):
                T.add_constraint(jacketsM[i])
            else:
                temp.remove_constraint(jacketsM[i])
                temp.add_constraint(jacketsS[i])
                if(temp.is_satisfiable()):
                    T.add_constraint(jacketsS[i])
                else:
                    temp.remove_constraint(jacketsS[i])

        #boots
        temp.add_constraint(bootsL[i])
        if(temp.is_satisfiable()):
            T.add_constraint(bootsL[i])
        else:
            temp.remove_constraint(bootsL[i])
            temp.add_constraint(bootsM[i])
            if(temp.is_satisfiable()):
                T.add_constraint(bootsM[i])
            else:
                temp.remove_constraint(bootsM[i])
                temp.add_constraint(bootsS[i])
                if(temp.is_satisfiable()):
                    T.add_constraint(bootsS[i])
                else:
                    temp.remove_constraint(bootsS[i])
            

    return T