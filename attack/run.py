import argparse

import rsiattack

attacks_box = {
    "admix": rsiattack.ADMIX,
    "bsr": rsiattack.BSR,
    "di2fgsm": rsiattack.DI2_FGSM,
    "ifgsm": rsiattack.I_FGSM,
    "mifgsm": rsiattack.MI_FGSM,
    "pgd": rsiattack.PGD,
    "pifgsm": rsiattack.PI_FGSM,
    "sifgsm": rsiattack.SI_FGSM,
    "ssa": rsiattack.SSA,
    "tifgsm": rsiattack.TI_FGSM,
    "sfcot": rsiattack.SFCoT,
}


def rsi_runner(model_type):
    parser = argparse.ArgumentParser(description="training the models to attack")
    parser.add_argument("--method", type=str, default="sfcot")
    #parser.add_argument("--l", type=int, default=l)
    parser.add_argument(
    "--model_type",
    type=str,
    default=model_type,
    # densenet121#inception_resv2
    help="used trainset in training",
    )
    args = parser.parse_args()
    attack_fun = attacks_box[args.method]
    attack = attack_fun(parser)
    attack.attack(model_type)
