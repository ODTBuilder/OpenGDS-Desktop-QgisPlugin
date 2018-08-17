# -*- coding: utf-8 -*-
"""
/***************************************************************************
 a
                                 A QGIS plugin
 aa
                             -------------------
        begin                : 2018-02-23
        copyright            : (C) 2018 by aa
        email                : aaa
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load a class from file a.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .aa import a
    return a(iface)
