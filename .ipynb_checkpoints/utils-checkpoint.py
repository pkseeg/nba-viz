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

team_colors = {
    'ATL': '#E03A3E', 'BOS': '#007A33', 'BKN': '#000000',
    'CHA': '#1D1160', 'CHI': '#CE1141', 'CLE': '#860038',
    'DAL': '#00538C', 'DEN': '#0E2240', 'DET': '#C8102E',
    'GSW': '#FFC72C', 'HOU': '#CE1141', 'IND': '#002D62',
    'LAC': '#C8102E', 'LAL': '#552583', 'MEM': '#5D76A9',
    'MIA': '#98002E', 'MIL': '#00471B', 'MIN': '#0C2340',
    'NOP': '#0C2340', 'NYK': '#006BB6', 'OKC': '#007AC1',
    'ORL': '#0077C0', 'PHI': '#006BB6', 'PHX': '#1D1160',
    'POR': '#E03A3E', 'SAC': '#5A2D81', 'SAS': '#C4CED4',
    'TOR': '#CE1141', 'UTA': '#000000', 'WAS': '#002B5C'
}    

name_swap = {
    'BRK': 'Brooklyn Nets',
    'BKN': 'Brooklyn Nets',
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
    'PHX': 'Phoenix Suns',
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
    'CHA': 'Charlotte Hornets',
    'NJN': 'New Jersey Nets'
}
temp = {}
for n in name_swap:
    temp[name_swap[n]] = n
for n in temp:
    name_swap[n] = temp[n]

all_team_ids = [k for k in name_swap]

ID_TO_TEAM_NBA = {'1610612761': 'TOR', '1610612743': 'DEN',
                  '1610612765': 'DET', '1610612740': 'NOP',
                  '1610612749': 'MIL', '1610612744': 'GSW',
                  '1610612759': 'SAS', '1610612757': 'POR',
                  '1610612746': 'LAC', '1610612742': 'DAL',
                  '1610612763': 'MEM', '1610612755': 'PHI',
                  '1610612738': 'BOS', '1610612750': 'MIN',
                  '1610612766': 'CHA', '1610612754': 'IND',
                  '1610612753': 'ORL', '1610612748': 'MIA',
                  '1610612745': 'HOU', '1610612758': 'SAC',
                  '1610612762': 'UTA', '1610612751': 'BKN',
                  '1610612737': 'ATL', '1610612756': 'PHX',
                  '1610612764': 'WAS', '1610612752': 'NYK',
                  '1610612760': 'OKC', '1610612747': 'LAL',
                  '1610612739': 'CLE', '1610612741': 'CHI'}

team_ids = {}
for i in ID_TO_TEAM_NBA:
    team_ids[ID_TO_TEAM_NBA[i]] = i


