# 07 Prove Milestone: Lists
def main ():
    # Get a chemical formula for a molecule from the user.
    molecule = input("Enter the molecular formula of the sample: ")
    # Get the mass of a chemical sample in grams from the user.
    grams = input("Enter the mass in grams of the sample: ")

    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    periodic_table_list = make_periodic_table()

    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    formula_list = parse_formula(molecule ,periodic_table_list)

    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(formula_list, periodic_table_list)

    # TODO: #27 Chemistry.py Prove 08 Compute the number of moles in the sample.

    # Print the molar mass.

    # Print the number of moles.





def make_periodic_table ():
    periodic_table_list = {
        # symbol: [name, atomic_mass]
        "Ac":	["Actinium",	227],
        "Ag":	["Silver",	107.8682],
        "Al":	["Aluminum",	26.9815386],
        "Ar":	["Argon",	39.948],
        "As":	["Arsenic",	74.9216],
        "At":	["Astatine",	210],
        "Au":	["Gold",	196.966569],
        "B":	["Boron",	10.811],
        "Ba":	["Barium",	137.327],
        "Be":	["Beryllium",	9.012182],
        "Bi":	["Bismuth",	208.9804],
        "Br":	["Bromine",	79.904],
        "C":	["Carbon",	12.0107],
        "Ca":	["Calcium",	40.078],
        "Cd":	["Cadmium",	112.411],
        "Ce":	["Cerium",	140.116],
        "Cl":	["Chlorine",	35.453],
        "Co":	["Cobalt",	58.933195],
        "Cr":	["Chromium",	51.9961],
        "Cs":	["Cesium",	132.9054519],
        "Cu":	["Copper",	63.546],
        "Dy":	["Dysprosium",	162.5],
        "Er":	["Erbium",	167.259],
        "Eu":	["Europium",	151.964],
        "F":	["Fluorine",	18.9984032],
        "Fe":	["Iron",	55.845],
        "Fr":	["Francium",	223],
        "Ga":	["Gallium",	69.723],
        "Gd":	["Gadolinium",	157.25],
        "Ge":	["Germanium",	72.64],
        "H":	["Hydrogen",	1.00794],
        "He":	["Helium",	4.002602],
        "Hf":	["Hafnium",	178.49],
        "Hg":	["Mercury",	200.59],
        "Ho":	["Holmium",	164.93032],
        "I":	["Iodine",	126.90447],
        "In":	["Indium",	114.818],
        "Ir":	["Iridium",	192.217],
        "K":	["Potassium",	39.0983],
        "Kr":	["Krypton",	83.798],
        "La":	["Lanthanum",	138.90547],
        "Li":	["Lithium",	6.941],
        "Lu":	["Lutetium",	174.9668],
        "Mg":	["Magnesium",	24.305],
        "Mn":	["Manganese",	54.938045],
        "Mo":	["Molybdenum",	95.96],
        "N":	["Nitrogen",	14.0067],
        "Na":	["Sodium",	22.98976928],
        "Nb":	["Niobium",	92.90638],
        "Nd":	["Neodymium",	144.242],
        "Ne":	["Neon",	20.1797],
        "Ni":	["Nickel",	58.6934],
        "Np":	["Neptunium",	237],
        "O":	["Oxygen",	15.9994],
        "Os":	["Osmium",	190.23],
        "P":	["Phosphorus",	30.973762],
        "Pa":	["Protactinium",	231.03588],
        "Pb":	["Lead",	207.2],
        "Pd":	["Palladium",	106.42],
        "Pm":	["Promethium",	145],
        "Po":	["Polonium",	209],
        "Pr":	["Praseodymium",	140.90765],
        "Pt":	["Platinum",	195.084],
        "Pu":	["Plutonium",	244],
        "Ra":	["Radium",	226],
        "Rb":	["Rubidium",	85.4678],
        "Re":	["Rhenium",	186.207],
        "Rh":	["Rhodium",	102.9055],
        "Rn":	["Radon",	222],
        "Ru":	["Ruthenium",	101.07],
        "S":	["Sulfur",	32.065],
        "Sb":	["Antimony",	121.76],
        "Sc":	["Scandium",	44.955912],
        "Se":	["Selenium",	78.96],
        "Si":	["Silicon",	28.0855],
        "Sm":	["Samarium",	150.36],
        "Sn":	["Tin",	118.71],
        "Sr":	["Strontium",	87.62],
        "Ta":	["Tantalum",	180.94788],
        "Tb":	["Terbium",	158.92535],
        "Tc":	["Technetium",	98],
        "Te":	["Tellurium",	127.6],
        "Th":	["Thorium",	232.03806],
        "Ti":	["Titanium",	47.867],
        "Tl":	["Thallium",	204.3833],
        "Tm":	["Thulium",	168.93421],
        "U":	["Uranium",	238.02891],
        "V":	["Vanadium",	50.9415],
        "W":	["Tungsten",	183.84],
        "Xe":	["Xenon",	131.293],
        "Y":	["Yttrium",	88.90585],
        "Yb":	["Ytterbium",	173.054],
        "Zn":	["Zinc",	65.38],
        "Zr":	["Zirconium",	91.224]}
    return periodic_table_list


class FormulaError(ValueError):
    """FormulaError is the type of error that
    parse_formula will raise if a formula is invalid.
    """


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound
    list that stores the quantity of atoms of each element
    in the molecule. For example, this function will convert
    "H2O" to [["H", 2], ["O", 1]] and
    "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]

    Parameters
        formula: a string that contains a chemical formula
        periodic_table_dict: the compound dictionary returned
            from make_periodic_table
    Return: a compound list that contains chemical symbols and
        quantities like this [["Fe", 2], ["O", 3]]
    """
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"

    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            start = index
            index += 1
            while index<len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elem_dict, symbol):
        return 0 if symbol not in elem_dict else elem_dict[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula,index+1,level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    curr = prev + group_dict[symbol] * quant
                    elem_dict[symbol] = curr
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError("invalid formula, "
                            f"unknown element symbol: {symbol}",
                            formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError("invalid formula, "
                        "unmatched close parenthesis",
                        formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula, illegal character"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError("invalid formula, "
                "unmatched open parenthesis",
                formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())


# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
    total_molar_mass = 0
    for symbol_key, element_list in symbol_quantity_list:
        atomic_symbol = element_list [0]
        quantity = element_list [1]
        # Get the atomic mass for the symbol from the dictionary.
        element_info = periodic_table_dict [atomic_symbol]
        atomic_mass = element_info [1]
        # Multiply the atomic mass by the quantity.
        total_element_mass = quantity * atomic_mass
        # Add the product into the total molar mass.
        total_molar_mass += total_element_mass
    # Return the total molar mass.
    return total_molar_mass


if __name__ == "__main__":
    main()