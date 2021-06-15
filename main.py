#СОЗДАНИЕ ПЕРВОЙ ФИГУРЫ
from bokeh.io import output_file
from bokeh.plotting import figure, show

# Рисунок будет отображен в статическом HTML-файле
output_file('Создание_первой_фигуры.html',
            title='Empty Bokeh Figure')

# Настроить общий объект figure()
fig = figure()

# Посмотрите, как это выглядит
show(fig)


#ПОДГОТОВКА ФИГУРЫ К ДАННЫМ
from bokeh.plotting import figure, show

output_file('Подготовка_фигуры_к_данным.html',
            title='Bokeh Figure')


fig = figure(background_fill_color='gray',
             background_fill_alpha=0.5,
             border_fill_color='blue',
             border_fill_alpha=0.25,
             plot_height=300,
             plot_width=500,
             x_axis_label='X Label',
             x_axis_type='datetime',
             x_axis_location='above',
             x_range=('2018-01-01', '2018-06-30'),
             y_axis_label='Y Label',
             y_axis_type='linear',
             y_axis_location='left',
             y_range=(0, 100),
             title='Example Figure',
             title_location='right',
             toolbar_location='below',
             tools='save')


show(fig)

#РИСОВАНИЕ ДАННЫХ С ПОМОЩЬЮ ГЛИФОВ
#Создание первых данных
from bokeh.io import output_file
from bokeh.plotting import figure, show

# Мои данные о координатах x-y
x = [1, 2, 1]
y = [1, 1, 2]


output_file('Рисование_данных_с_помощью_глифов1.html', title='First Glyphs')

# Создайте фигуру без панели инструментов и диапазонов осей
fig = figure(title='My Coordinates',
             plot_height=300, plot_width=300,
             x_range=(0, 3), y_range=(0, 3),
             toolbar_location=None)

# Нарисуйте координаты в виде кругов
fig.circle(x=x, y=y,
           color='green', size=10, alpha=0.5)

# Показать сюжет
show(fig)

#Создание вторых данных
import numpy as np
from bokeh.plotting import figure, show

# Мои данные о подсчете слов
day_num = np.linspace(1, 10, 10)
daily_words = [450, 628, 488, 210, 287, 791, 508, 639, 397, 943]
cumulative_words = np.cumsum(daily_words)


output_file('Рисование_данных_с_помощью_глифов2.html', title='First Glyphs')

# Создаем фигуру с осью x типа datetime
fig = figure(title='My Tutorial Progress',
             plot_height=400, plot_width=700,
             x_axis_label='Day Number', y_axis_label='Words Written',
             x_minor_ticks=2, y_range=(0, 6000),
             toolbar_location=None)

# Ежедневные слова будут представлены в виде вертикальных полос (столбцов)
fig.vbar(x=day_num, bottom=0, top=daily_words,
         color='blue', width=0.75,
         legend='Daily')

# Накопленная сумма будет линией тренда
fig.line(x=day_num, y=cumulative_words,
         color='gray', line_width=1,
         legend='Cumulative')

# Поместите легенду в левый верхний угол
fig.legend.location = 'top_left'

# Давайте проверим
show(fig)


#НЕБОЛЬШАЯ ЗАМЕТКА О ДАННЫХ
import pandas as pd
# Прочитать csv файлы
player_stats = pd.read_csv('2017-18_playerBoxScore.csv', parse_dates=['gmDate'])
team_stats = pd.read_csv('2017-18_teamBoxScore.csv', parse_dates=['gmDate'])
standings = pd.read_csv('2017-18_standings.csv', parse_dates=['stDate'])
print(player_stats)


#ИСПОЛЬЗОВАНИЕ ОБЪЕКТА ColumnDataSource
#Пример 1
west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') | (standings['teamAbbr'] == 'GS')]
              .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
             .sort_values(['teamAbbr','stDate']))
print(west_top_2.head())


from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource

# Output to file
output_file('west-top-2-standings-race1.html',
            title='Western Conference Top 2 Teams Wins Race')

# Isolate the data for the Rockets and Warriors
rockets_data = west_top_2[west_top_2['teamAbbr'] == 'HOU']
warriors_data = west_top_2[west_top_2['teamAbbr'] == 'GS']

# Create a ColumnDataSource object for each team
rockets_cds = ColumnDataSource(rockets_data)
warriors_cds = ColumnDataSource(warriors_data)

# Create and configure the figure
fig = figure(x_axis_type='datetime',
             plot_height=300, plot_width=600,
             title='Western Conference Top 2 Teams Wins Race, 2017-18',
             x_axis_label='Date', y_axis_label='Wins',
             toolbar_location=None)

# Render the race as step lines
fig.step('stDate', 'gameWon',
         color='#CE1141', legend='Rockets',
         source=rockets_cds)
fig.step('stDate', 'gameWon',
         color='#006BB6', legend='Warriors',
         source=warriors_cds)

# Move the legend to the upper left corner
fig.legend.location = 'top_left'

# Show the plot
show(fig)
#Пример 2
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Вывод в файл
output_file('west-top-2-standings-race2.html',
            title='Western Conference Top 2 Teams Wins Race')

# Создать ColumnDataSource
west_cds = ColumnDataSource(west_top_2)

# Создайте представления для каждой команды
rockets_view = CDSView(source=west_cds,
                       filters=[GroupFilter(column_name='teamAbbr', group='HOU')])
warriors_view = CDSView(source=west_cds,
                        filters=[GroupFilter(column_name='teamAbbr', group='GS')])

# Создаем и настраиваем фигуру
west_fig = figure(x_axis_type='datetime',
                  plot_height=300, plot_width=600,
                  title='Western Conference Top 2 Teams Wins Race, 2017-18',
                  x_axis_label='Date', y_axis_label='Wins',
                  toolbar_location=None)

# Отрисовываем гонку в виде ступенчатых линий
west_fig.step('stDate', 'gameWon',
              source=west_cds, view=rockets_view,
              color='#CE1141', legend='Rockets')
west_fig.step('stDate', 'gameWon',
              source=west_cds, view=warriors_view,
              color='#006BB6', legend='Warriors')

# Переместите легенду в верхний левый угол
west_fig.legend.location = 'top_left'

# Показать сюжет
show(west_fig)

#ОРГАНИЗАЦИЯ НЕСКОЛЬКИХ ВИЗУАЛИЗАЦИЙ С ПОМОЩЬЮ МАКЕТОВ
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Вывод в файл
output_file('Организация_нескольких_визуализаций_с_помощью_макетов.html',
            title='Eastern Conference Top 2 Teams Wins Race')

# Создать ColumnDataSource
standings_cds = ColumnDataSource(standings)

# Create views for each team
celtics_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr',
                                           group='BOS')])
raptors_view = CDSView(source=standings_cds,
                      filters=[GroupFilter(column_name='teamAbbr',
                                           group='TOR')])

# Создаем и настраиваем фигуру
east_fig = figure(x_axis_type='datetime',
           plot_height=300, plot_width=600,
           title='Eastern Conference Top 2 Teams Wins Race, 2017-18',
           x_axis_label='Date', y_axis_label='Wins',
           toolbar_location=None)

# Отрисовываем гонку в виде ступенчатых линий
east_fig.step('stDate', 'gameWon',
              color='#007A33', legend='Celtics',
              source=standings_cds, view=celtics_view)
east_fig.step('stDate', 'gameWon',
              color='#CE1141', legend='Raptors',
              source=standings_cds, view=raptors_view)

# Переместите легенду в верхний левый угол
east_fig.legend.location = 'top_left'

# Показать сюжет
show(east_fig)

#ДОБАВЛЕНИЕ ВЗАИМОДЕЙСТВИЯ
#ВЫБОР ТОЧЕК ДАННЫХ
# Найдите игроков, которые сделали хотя бы 1 трехочковый бросок за сезон
three_takers = player_stats[player_stats['play3PA'] > 0]

# Убрать имена игроков, поместив их в один столбец
three_takers['name'] = [f'{p["playFNm"]} {p["playLNm"]}'
                        for _, p in three_takers.iterrows()]

# Суммируйте общее количество трехочковых попыток и количество попыток для каждого игрока
three_takers = (three_takers.groupby('name')
                            .sum()
                            .loc[:,['play3PA', 'play3PM']]
                            .sort_values('play3PA', ascending=False))

# Отфильтровать всех, кто не сделал хотя бы 100 трехочковых бросков
three_takers = three_takers[three_takers['play3PA'] >= 100].reset_index()

# Добавить столбец с рассчитанным трехбалльным процентом (выполнено / предпринято)
three_takers['pct3PM'] = three_takers['play3PM'] / three_takers['play3PA']
print(three_takers.sample(5))



# Выбор группы игроков в раздаче из полученного DataFrame, при этом отключить цвет глифов
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter

# Файл вывода
output_file('Выбор_точек_данных.html',
            title='Three-Point Attempts vs. Percentage')

# Сохраним данные в ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)

# Укажите инструменты выбора, которые будут доступны
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

# Создание картинки
fig = figure(plot_height=400,
             plot_width=600,
             x_axis_label='Three-Point Shots Attempted',
             y_axis_label='Percentage Made',
             title='3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-18',
             toolbar_location='below',
             tools=select_tools)

# Отформатируйте метки делений оси Y в процентах
fig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# Добавить квадрат, представляющий каждого игрока
fig.square(x='play3PA',
           y='pct3PM',
           source=three_takers_cds,
           color='royalblue',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=0.3)

# Показать результат
show(fig)

#ДОБАВЛЕНИЕ ДЕЙСТВИЙ ПРИ НАВЕДЕНИИ КУРСОРА
from bokeh.models import HoverTool

output_file('Добавление_действий_при_наведении_курсора.html',
            title='Three-Point Attempts vs. Percentage')

# Отформатируйте всплывающую подсказку
# Отформатируйте всплывающую подсказку
tooltips = [
            ('Player','@name'),
            ('Three-Pointers Made', '@play3PM'),
            ('Three-Pointers Attempted', '@play3PA'),
            ('Three-Point Percentage','@pct3PM{00.0%}'),
           ]

# Настроить рендерер, который будет использоваться при наведении
hover_glyph = fig.circle(x='play3PA', y='pct3PM', source=three_takers_cds,
                         size=15, alpha=0,
                         hover_fill_color='black', hover_alpha=0.5)

# Добавляем HoverTool к фигуре
fig.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))

# Показать
show(fig)

#ВЫДЕЛЕНИЕ ДАННЫХ С ПОМОЩЬЮ ЛЕГЕНДЫ
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.layouts import row

# Вывести в записной книжке
output_file('lebron-vs-durant.html',
            title='LeBron James vs. Kevin Durant')

# Хранить данные в ColumnDataSource
player_gm_stats = ColumnDataSource(player_stats)

# Создайте представление для каждого игрока
lebron_filters = [GroupFilter(column_name='playFNm', group='LeBron'),
                  GroupFilter(column_name='playLNm', group='James')]
lebron_view = CDSView(source=player_gm_stats,
                      filters=lebron_filters)

durant_filters = [GroupFilter(column_name='playFNm', group='Kevin'),
                  GroupFilter(column_name='playLNm', group='Durant')]
durant_view = CDSView(source=player_gm_stats,
                      filters=durant_filters)
# Объединить общие аргументы ключевых слов в dicts
common_figure_kwargs = {
    'plot_width': 400,
    'x_axis_label': 'Points',
    'toolbar_location': None,
}
common_circle_kwargs = {
    'x': 'playPTS',
    'y': 'playTRB',
    'source': player_gm_stats,
    'size': 12,
    'alpha': 0.7,
}
common_lebron_kwargs = {
    'view': lebron_view,
    'color': '#002859',
    'legend': 'LeBron James'
}
common_durant_kwargs = {
    'view': durant_view,
    'color': '#FFC324',
    'legend': 'Kevin Durant'
}

# Создайте две фигуры и нарисуйте данные
hide_fig = figure(**common_figure_kwargs,
                  title='Click Legend to HIDE Data',
                  y_axis_label='Rebounds')
hide_fig.circle(**common_circle_kwargs, **common_lebron_kwargs)
hide_fig.circle(**common_circle_kwargs, **common_durant_kwargs)

mute_fig = figure(**common_figure_kwargs, title='Click Legend to MUTE Data')
mute_fig.circle(**common_circle_kwargs, **common_lebron_kwargs,
                muted_alpha=0.1)
mute_fig.circle(**common_circle_kwargs, **common_durant_kwargs,
                muted_alpha=0.1)

# Добавляем интерактивности в легенду
hide_fig.legend.click_policy = 'hide'
mute_fig.legend.click_policy = 'mute'

# Визуализировать
show(row(hide_fig, mute_fig))