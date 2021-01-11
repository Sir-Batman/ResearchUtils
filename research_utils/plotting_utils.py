import matplotlib.pyplot as plt
from pathlib import Path
from subprocess import call


def make_3d_spinner(ax, tmpdir="/tmp", output="out.mp4"):
    """
    Takes a 3d axis and renders a spinning animation about the Z-axis using ffmpeg
    Note that if the output file container type is to be changed (ie .mkv instead of .mp4)
    changing the extension of the output filename will be reflected in the final output
    because ffmpeg is smart like that.

    :param ax: 3D axis object to be rendered
    :param tmpdir: Location where the .png's of each frame of the animation are stored
    :param output: path to the output file.
    :return: The returncode from the call to ffmpeg
    """
    tmpdir = Path(tmpdir)
    for i in range(0, 360):
        ax.view_init(elev=10, azim=i)
        save_path = tmpdir.joinpath(Path(f"movie{i:03d}.png"))
        plt.savefig(save_path)
    image_path = str(tmpdir) + r"/movie%03d.png"
    return call(["ffmpeg", "-r", '20', '-i', image_path, str(output)])


def shaded_error_plot(ax, x, y, yerr, label='', color='red'):
    """
    TODO fill this in

    :param ax:
    :param x:
    :param y:
    :param yerr:
    :param label:
    :param color:
    :return:
    """
    ax.plot(x, y, label=label, c=color)
    ax.fill_between(x, y-yerr, y+yerr, alpha=0.3, facecolor=color)
    return ax
