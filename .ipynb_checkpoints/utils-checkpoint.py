import matplotlib.pyplot as plt
import pandas as pd

MAIN = '#753BBD'
OTHER = '#954E4C'
BACKGROUND = '#006272'

def set_size(w,h, ax=None):
    """ w, h: width, height in inches """
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

name_swap = {
    'BRK': 'Brooklyn Nets',
    'WAS': 'Washington Wizards',
    'CHI': 'Chicago Bulls',
    'MIA': 'Miami Heat',
    'NYK': 'New York Knicks',
    'CHO': 'Charlotte Hornets',
    'BOS': 'Boston Celtics',
    'CLE': 'Cleveland Cavaliers',
    'MIL': 'Milwaukee Bucks',
    'PHI': 'Philadelphia 76ers',
    'ATL': 'Atlanta Hawks',
    'TOR': 'Toronto Raptors',
    'IND': 'Indiana Pacers',
    'DET': 'Detroit Pistons',
    'ORL': 'Orlando Magic',
    'GSW': 'Golden State Warriors',
    'PHO': 'Phoenix Suns',
    'UTA': 'Utah Jazz',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'LAC': 'Los Angeles Clippers',
    'POR': 'Portland Trail Blazers',
    'MEM': 'Memphis Grizzlies',
    'LAL': 'Los Angeles Lakers',
    'MIN': 'Minnesota Timberwolves',
    'OKC': 'Oklahoma City Thunder',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'NOP': 'New Orleans Pelicans',
    'HOU': 'Houston Rockets',
    'SEA': 'Seattle SuperSonics',
    'NOH': 'New Orleans Hornets',
    'CHA': 'Charlotte Bobcats',
    'NJN': 'New Jersey Nets'
}
temp = {}
for n in name_swap:
    temp[name_swap[n]] = n
for n in temp:
    name_swap[n] = temp[n]

all_team_ids = [k for k in name_swap]