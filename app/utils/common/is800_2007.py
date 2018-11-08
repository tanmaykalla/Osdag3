class IS800_2007(object):

# =============================================================
#    SECTION  1     GENERAL
# =============================================================
#    SECTION  2     MATERIALS
# =============================================================
#    SECTION  3     GENERAL DESIGN REQUIREMENTS
# =============================================================
#    SECTION  4     METHODS OF STRUCTURAL ANALYSIS
# =============================================================
#    SECTION  5     LIMIT STATE DESIGN
# =============================================================
#    SECTION  6     DESIGN OF TENSION MEMBERS
# =============================================================
#    SECTION  7     DESIGN OF COMPRESS1ON MEMBERS
# =============================================================
#    SECTION  8     DESIGN OF MEMBERS SUBJECTED TO BENDING
# =============================================================
#    SECTION  9     MEMBER SUBJECTED TO COMBINED FORCES
# =============================================================
#    SECTION  10    CONNECTIONS
# =============================================================
#    SECTION  11    WORKING STRESS DESIGN
# =============================================================
#    SECTION  12    DESIGN AND DETAILING FOR EARTHQUAKE
# =============================================================
#    SECTION  13    FATIGUE
# =============================================================
#    SECTION  14    DESIGN ASSISTED BY TESTING
# =============================================================
#    SECTION  15    DURABILITY
# =============================================================
#    SECTION  16    FIRE RESISTANCE
# =============================================================
#    SECTION  17    FABRICATION AND ERECTION
# =============================================================
#    ANNEX  A       LIST OF REFERRED INDIAN STANDARDS
# =============================================================
#    ANNEX  B       ANALYSIS AND DESIGN METHODS
# =============================================================
#    ANNEX  C       DESIGN AGAINST FLOOR VIBRATION
# =============================================================
#    ANNEX  D       DETERMINATION OF EFFECTIVE LENGTH OF COLUMNS
# =============================================================
#    ANNEX  E       ELASTIC LATERAL TORSIONAL BUCKLING
# =============================================================
#    ANNEX  F       CONNECTIONS
# =============================================================
#    ANNEX  G       GENERAL RECOMMENDATIONS FOR STEELWORK TENDERS AND CONTRACTS
# =============================================================
#    ANNEX  H       PLASTIC PROPERTIES OF BEAMS
# =============================================================
#------------------END------------------




@staticmethod
    def compute_min_weld_thickness(part1_thickness, part2_thickness):
        thicker_part_thickness = max(part1_thickness, part2_thickness)

        if thicker_part_thickness <= 10:
            return 3
        elif thicker_part_thickness <= 20:
            return 5
        elif thicker_part_thickness <= 32:
            return 6
        elif thicker_part_thickness <= 50:
            return 10

    @staticmethod
    def compute_max_weld_thickness(part1_thickness, part2_thickness):
        return min(part1_thickness, part2_thickness)