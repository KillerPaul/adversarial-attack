import argparse

import attack

attacks_box = {
    "admix": attack.ADMIX,
    "bsr": attack.BSR,
    "di2fgsm": attack.DI2_FGSM,
    "ifgsm": attack.I_FGSM,
    "mifgsm": attack.MI_FGSM,
    "pgd": attack.PGD,
    "pifgsm": attack.PI_FGSM,
    "sifgsm": attack.SI_FGSM,
    "ssa": attack.SSA,
    "tifgsm": attack.TI_FGSM,
    "sfcot": attack.SFCoT,
    "cstransform": attack.CSTransform,
}


def rsi_runner(model_type):
    parser = argparse.ArgumentParser(description="training the models to attack")
    parser.add_argument("--method", type=str, default="cstransform")
    parser.add_argument(
    "--model_type",
    type=str,
    default=model_type,
    help="used trainset in training",
    )
    args = parser.parse_args()
    attack_fun = attacks_box[args.method]
    attack = attack_fun(parser)
    attack.attack(model_type)
