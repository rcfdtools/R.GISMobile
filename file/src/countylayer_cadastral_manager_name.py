# https://github.com/rcfdtools
# Get layer from https://www.datos.gov.co/Ordenamiento-Territorial/Gestores-Catastrales-de-Colombia/bhcx-bx97/about_data
# QGIS replace full text field for cadastral names
# Run from Field Calculator and create a string text field (255) with the name Cadastre

from qgis.core import *
from qgis.gui import *

@qgsfunction(group='Custom', referenced_columns=[])

def cadastre_replace_txt(field):
    # Replacement list
    replacement_list = [['AREA METROPOLITANA DE BARRANQUILLA AMB', 'Área Metropolitana de Barranquilla AMB'],
                        ['AREA METROPOLITANA DE BUCARAMANGA AMB', 'Área Metropolitana de Bucaramanga AMB'],
                        ['AREA METROPOLITANA DE CENTRO OCCIDENTE AMCO', 'Área Metropolitana de Centro Occidente AMCO'],
                        ['AREA METROPOLITANA DE VALLE DE ABURRA AMV', 'Área Metropolitana de Valle de Aburra AMV'],
                        ['ASOMUNICIPIOS', 'ASOMUNICIPIOS'],
                        ['CATASTRO ANTIOQUIA', 'Catastro Antioquia'],
                        ['CATASTRO DE MEDELLIN', 'Catastro de Medellín'],
                        ['CATASTRO MUNICIPAL DE CALI', 'Catastro Municipal de Cali'],
                        ['DEPARTAMENTO DE CUNDINAMARCA', 'Departamento de Cundinamarca'],
                        ['DEPARTAMENTO DEL VALLE DEL CAUCA', 'Departamento del Valle del Cauca'],
                        ['DISTRITO DE BARRANQUILLA', 'Distrito de Barranquilla'],
                        ['DISTRITO TURISTICO, CULTURAL E HISTORICO DE SANTA MARTA', 'Distrito Turístico, Cultural e Histórico de Santa Marta'],
                        ['IGAC', 'IGAC'],
                        ['MUNICIPIO ARMENIA', 'Municipio Armenia'],
                        ['MUNICIPIO DE BARRANCABERMEJA', 'Municipio de Barrancabermeja'],
                        ['MUNICIPIO DE CHIQUINQUIRA', 'Municipio de Chiquinquirá'],
                        ['MUNICIPIO DE CHIRIGÜANA', 'Municipio de Chirigüana'],
                        ['MUNICIPIO DE COTA', 'Municipio de Cota'],
                        ['MUNICIPIO DE ENVIGADO', 'Municipio de Envigado'],
                        ['MUNICIPIO DE FLORENCIA', 'Municipio de Florencia'],
                        ['MUNICIPIO DE FLORIDABLANCA', 'Municipio de Floridablanca'],
                        ['MUNICIPIO DE FUSAGASUGA', 'Municipio de Fusagasuga'],
                        ['MUNICIPIO DE GARZON', 'Municipio de Garzón'],
                        ['MUNICIPIO DE GIRARDOT', 'Municipio de Girardot'],
                        ['MUNICIPIO DE IBAGUE', 'Municipio de Ibague'],
                        ['MUNICIPIO DE JAMUNDI', 'Municipio de Jamundi'],
                        ['MUNICIPIO DE MALAGA', 'Municipio de Malaga'],
                        ['MUNICIPIO DE MONTERIA', 'Municipio de Montería'],
                        ['MUNICIPIO DE NEIVA', 'Municipio de Neiva'],
                        ['MUNICIPIO DE RIONEGRO', 'Municipio de Rionegro'],
                        ['MUNICIPIO DE SABANALARGA', 'Municipio de Sabanalarga'],
                        ['MUNICIPIO DE SABANETA', 'Municipio de Sabaneta'],
                        ['MUNICIPIO DE SAHAGUN', 'Municipio de Sahagun'],
                        ['MUNICIPIO DE SAN JOSE DE CUCUTA', 'Municipio de San José de Cucuta'],
                        ['MUNICIPIO DE SESQUILE', 'Municipio de Sesquilé'],
                        ['MUNICIPIO DE SINCELEJO', 'Municipio de Sincelejo'],
                        ['MUNICIPIO DE SOACHA', 'Municipio de Soacha'],
                        ['MUNICIPIO DE SOLEDAD', 'Municipio de Soledad'],
                        ['MUNICIPIO DE TUNJA', 'Municipio de Tunja'],
                        ['MUNICIPIO DE VALLEDUPAR', 'Municipio de Valledupar'],
                        ['MUNICIPIO DE VILLAVICENCIO', 'Municipio de Villavicencio'],
                        ['MUNICIPIO DE ZIPAQUIRA', 'Municipio de Zipaquirá'],
                        ['MUNICIPIO MARINILLA', 'Municipio Marinilla'],
                        ['MUNICIPIOS ASOCIADOS DEL ALTIPLANO DEL ORIENTE ANTIOQUEÑO MASORA', 'Municipios Asociados del Altiplano del Oriente Antioqueño Masora'],
                        ['UNIDAD ADMINISTRATIVA ESPECIAL DE CATASTRO DISTRITAL BOGOTA UAECD', 'Unidad Administrativa Especial de Catastro Distrital Bogota UAECD']
                       ]
    for i in replacement_list:
        val = True
        #if field.upper().find(i[0].upper()) > 0 and val:
        if field.upper() == i[0].upper() and val:
            val = False
            return i[1]