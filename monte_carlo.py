from numpy.random import normal
from numpy import array
import numpy

import math




def plotstock(ticker='PG', time_intervals=1000, iterations=10, start='2007-1-1'):
    # Load data for 'ticker'
    data = pd.DataFrame()
    data[ticker] = wb.DataReader(ticker, data_source='yahoo', start=start)['Adj Close']
    
    # Estimate historical log returns
    log_returns = np.log(1 + data.pct_change())
    
    #data.plot(figsize=(10, 6));
    #log_returns.plot(figsize=(10, 6));
    
    # Calculate brownian motion --> r = drift + stdev * e**r
    u = log_returns.mean()
    var = log_returns.var()
    drift = u - (0.5 * var)
    stdev = log_returns.std()    
    daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(time_intervals, iterations)))

    # Fill matrix of dims time_intervals x iterations
    price_list = np.zeros_like(daily_returns)
    
    # stock price in new list must be last one in data set to 
    # make reasonable predictions, also must be first in list 
    # for all iterations
    price_list[0] = data.iloc[-1]
    
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]
        
    # Combine historical data with predicted data
    pred_date = pd.date_range(start = data.index.max().date(), 
                               periods = time_intervals)

    #preds = pd.DataFrame(price_list)
    #preds['Date'] = pred_date
    #preds = preds.set_index('Date')
    #combined_data = data.append(preds, sort=False)
    #return combined_data

    sim = []
    for i in range(len(price_list)):
        for j in range(len(price_list[i])):
            v = {'Date':pred_date[i].date(), ticker:price_list[i][j]}
            sim.append(v)
    sim = pd.DataFrame(sim).set_index('Date')
    means = sim.reset_index().groupby('Date')[[ticker]].mean()
    
    data_dates = data.reset_index().Date.apply(lambda x: datetime.datetime.strftime(x, "%x")).values
    sim_dates = sim.reset_index().Date.apply(lambda x: datetime.datetime.strftime(x, "%x")).values
    mean_dates = means.reset_index().Date.apply(lambda x: datetime.datetime.strftime(x, "%x")).values

    dd = {'actual': [data_dates, data[ticker].values],
            'simulated': [sim_dates, sim[ticker].values],
            'means': [mean_dates, means[ticker].values]}
    return dd
    # Make plotly plot
#     trace0 = go.Scatter(
#         x=dd['actual'][0],
#         y=dd['actual'][1]
#     )
#     trace1 = go.Scatter(
#         x=dd['simulated'][0],
#         y=combo['simulated'][1]
#     )
#     trace2 = go.Scatter(
#         x=dd['means'][0],
#         y=dd['means'][1]
#     )
#     plotdata = [trace0, trace1, trace2]
#     plotty = py.plot(plotdata, filename=f'{ticker}-line', auto_open=False)
#     return plotty
#     return tls.get_embed(plotty)
#     return dd




def pyplotstock(ticker='PG', time_intervals=1000, iterations=10, start='2007-1-1'):
    # Load data for 'ticker'
    data = pd.DataFrame()
    data[ticker] = wb.DataReader(ticker, data_source='yahoo', start=start)['Adj Close']
    
    # Estimate historical log returns
    log_returns = np.log(1 + data.pct_change())
    
    #data.plot(figsize=(10, 6));
    #log_returns.plot(figsize=(10, 6));
    
    # Calculate brownian motion --> r = drift + stdev * e**r
    u = log_returns.mean()
    var = log_returns.var()
    drift = u - (0.5 * var)
    stdev = log_returns.std()    
    daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(time_intervals, iterations)))

    # Fill matrix of dims time_intervals x iterations
    price_list = np.zeros_like(daily_returns)
    
    # stock price in new list must be last one in data set to 
    # make reasonable predictions, also must be first in list 
    # for all iterations
    price_list[0] = data.iloc[-1]
    
    for t in range(1, t_intervals):
        price_list[t] = price_list[t - 1] * daily_returns[t]
        
    # Combine historical data with predicted data
    pred_date = pd.date_range(start = data.index.max().date(), 
                               periods = time_intervals)

    preds = pd.DataFrame(price_list)
    preds['Date'] = pred_date
    preds = preds.set_index('Date')
    combined_data = data.append(preds, sort=False)

    sim = []
    for i in range(len(price_list)):
        for j in range(len(price_list[i])):
            v = {'Date':pred_date[i].date(), ticker:price_list[i][j]}
            sim.append(v)
    sim = pd.DataFrame(sim).set_index('Date')
    means = sim.reset_index().groupby('Date')[[ticker]].mean()
    
    # Plot data
    plt.figure(figsize=(10,6))
    plt.title(ticker)
    plt.plot(data)
    plt.plot(sim, alpha=0.5);
    plt.plot(means);
#     plt.plot(combined_data);
    plt.savefig(f'static/img/{ticker}-{datetime.datetime.now().date()}.png')
    return combined_data




def monte_carlo_step(previous, rate, stdv):
    return previous * math.exp(normal(rate, stdv))

def build_monte_carlo_array(previous, rate, stdv, depth):
    sim_series = [monte_carlo_step(previous, rate, stdv)]
    for i in range(depth):
        sim_series.append(monte_carlo_step(sim_series[i], rate, stdv))
    return array([sim_series])
