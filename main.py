from video_display import DisplayVideo
from video_display import Editors


def get_editors():
    editors = list()

    editors.append(Editors.gray)
    editors.append(Editors.gauss)
    editors.append(Editors.adaptive_treshold)
    editors.append(Editors.sharpen)

    return editors

if __name__ == '__main__':
    # 0 for the default webcamera
    source = 0
    dv = DisplayVideo(source)

    dv.editors = get_editors()
    dv.start()
