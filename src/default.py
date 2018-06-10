################################################################################
#      This file is part of CoreELEC - https://coreelec.org
#      Copyright (C) 2018-present CoreELEC (team (at) coreelec.org)
#      Copyright (C) 2009-2013 Stephan Raue (stephan@openelec.tv)
#      Copyright (C) 2013 Lutz Fiebach (lufie@openelec.tv)
#
#  CoreELEC is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  CoreELEC is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with CoreELEC.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import xbmc
import socket
import xbmcaddon

__scriptid__ = 'service.coreelec.settings'
__addon__ = xbmcaddon.Addon(id=__scriptid__)
__cwd__ = __addon__.getAddonInfo('path')
__media__ = '%s/resources/skins/Default/media/' % __cwd__
_ = __addon__.getLocalizedString

try:
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect('/var/run/service.coreelec.settings.sock')
    sock.send('openConfigurationWindow')
    sock.close()
except Exception, e:
    xbmc.executebuiltin('Notification("CoreELEC", "%s", 5000, "%sicons/icon.png")' % (_(32390).encode('utf-8'), __media__))
