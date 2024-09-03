# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# import combined results and get overview
results = pd.read_excel("C:\\02_HIWI_Research\\04_RECC\\RECC_Results\\Combined\\RECC_results_combined.xlsx")
print(results.columns)
results.info()

# import years
years = results.columns[8:] # Selecting all columns from the year 2015 onwards up to 2060

# DEFINE TRANSPORT DEMAND DATAFRAME (Vkt)
# for comparison of all km within the city limits of Freiburg
# CE stands for Circular Economy Strategies, including Car Sharing, higher parking costs etc.
vkt_total = results[results['Indicator'].str.contains('vehicle-km driven by pass. vehicles', case=False)]
vkt_withCE = vkt_total[vkt_total['CE strat'].str.contains('with CE', case=False)
                       & vkt_total['ClimPol scen'].str.contains('baseline', case=False)]
vkt_noCE = vkt_total[~vkt_total['CE strat'].str.contains('with CE', case=False)
                     & vkt_total['ClimPol scen'].str.contains('baseline', case=False)]

def Transport_demand_Vkt_plots():
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in vkt_withCE.iterrows():
        plt.plot(years, row[8:], label=f"{row['SocEc scen']}")
        
    # edit the plot
    plt.title('Development of "vehicle-km driven by pass. vehicles" Over the Years, with CE strategies')
    plt.xlabel('Year')
    plt.ylabel('Vehicle-km')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in vkt_noCE.iterrows():
        plt.plot(years, row[8:], label=f"{row['SocEc scen']}")
        
    # edit the plot
    plt.title('Development of "vehicle-km driven by pass. vehicles" Over the Years, no CE strategies')
    plt.xlabel('Year')
    plt.ylabel('Vehicle-km')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)

    # Show the plot
    plt.tight_layout()
    plt.show()
    
# DEFINE Passenger-km DATAFRAME
# Pkm is Vkt *  Occupancy Rate resulting in total transport service measurement unit
pkm_total = results[results['Indicator'].str.contains('passenger-km supplied by pass. vehicles', case=False)]

pkm_withCE = pkm_total[pkm_total['CE strat'].str.contains('with CE', case=False)
                       & pkm_total['ClimPol scen'].str.contains('baseline', case=False)]
pkm_noCE = pkm_total[~pkm_total['CE strat'].str.contains('with CE', case=False)
                     & pkm_total['ClimPol scen'].str.contains('baseline', case=False)]

def Transport_Service_Pkm_plots():
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in pkm_withCE.iterrows():
        plt.plot(years, row[8:], label=f"{row['SocEc scen']}")
        
    # edit the plot
    plt.title('Development of "passenger-km supplied by pass. vehicles" Over the Years, with CE strategies')
    plt.xlabel('Year')
    plt.ylabel('Vehicle-km')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in pkm_noCE.iterrows():
        plt.plot(years, row[8:], label=f"{row['SocEc scen']}")
        
    # edit the plot
    plt.title('Development of "passenger-km supplied by pass. vehicles" Over the Years, no CE strategies')
    plt.xlabel('Year')
    plt.ylabel('Vehicle-km')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    
# DEFINE GHG-EMISSIONS DATAFRAME
results_ghg_rcp = results[results['ClimPol scen'].str.contains('rcp', case=False) 
                          & results['Indicator'].str.contains('GHG emissions, vehicles, use phase _7d', case=False)]
results_ghg_baseline = results[results['ClimPol scen'].str.contains('baseline', case=False) 
                               & results['Indicator'].str.contains('GHG emissions, vehicles, use phase _7d', case=False)] 

def GHG_Emissions_use_phase_plots():
    # PLOT FIGURE BASELINE
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in results_ghg_baseline.iterrows():
        plt.plot(years, row[8:], label = f"{row['SocEc scen']} - {row['CE strat']}")
    
    # edit the plot
    plt.title('Development of "GHG emissions, vehicles, use phase _7d" Over the Years for Baseline Scenarios')
    plt.xlabel('Year')
    plt.ylabel('Mt CO2-eq.')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # PLOT FIGURE RCP
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in results_ghg_rcp.iterrows():
        plt.plot(years, row[8:], label = f"{row['SocEc scen']} - {row['CE strat']}")
    
    # edit the plot
    plt.title('Development of "GHG emissions, vehicles, use phase _7d" Over the Years for RCP2.6 scenarios')
    plt.xlabel('Year')
    plt.ylabel('Mt CO2-eq.')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()


# DEFINE VEHICLE STOCK BASELINE DATAFRAME
# for battery electric, gasoline, diesel
results_stock_baseline_LED = results[results['ClimPol scen'].str.contains('baseline', case=False) 
                                     & results['SocEc scen'].str.contains('LED', case=False) 
                                     & results['Indicator'].str.contains('In-use stock', case=False) 
                                     & results['Indicator'].str.contains('ICEG|ICED|BEV', case=False, regex=True)]
results_stock_baseline_SSP1 = results[results['ClimPol scen'].str.contains('baseline', case=False) 
                                      & results['SocEc scen'].str.contains('SSP1', case=False) 
                                      & results['Indicator'].str.contains('In-use stock', case=False) 
                                      & results['Indicator'].str.contains('ICEG|ICED|BEV', case=False, regex=True)]
results_stock_baseline_SSP2 = results[results['ClimPol scen'].str.contains('baseline', case=False)
                                      & results['SocEc scen'].str.contains('SSP2', case=False) 
                                      & results['Indicator'].str.contains('In-use stock', case=False) 
                                      & results['Indicator'].str.contains('ICEG|ICED|BEV', case=False, regex=True)]
   
def Vehicle_stock_baseline_plots():
 
    # PLOT FIGURE BASELINE LED
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in results_stock_baseline_LED.iterrows():
        plt.plot(years, row[8:], label=f"{row['Indicator']} - {row['CE strat']}")
    
    # edit the plot
    plt.title('Development of "Vehicle Stocks for Gasoline, Diesel and BEVs" Over the Years for baseline LED scenario')
    plt.xlabel('Year')
    plt.ylabel('Million vehicles')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # PLOT FIGURE BASELINE SSP1
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in results_stock_baseline_SSP1.iterrows():
        plt.plot(years, row[8:], label=f"{row['Indicator']} - {row['CE strat']}")
    
    # edit the plot
    plt.title('Development of "Vehicle Stocks for Gasoline, Diesel and BEVs" Over the Years for baseline SSP1 scenario')
    plt.xlabel('Year')
    plt.ylabel('Million vehicles')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # PLOT FIGURE BASELINE SSP2
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in results_stock_baseline_SSP2.iterrows():
        plt.plot(years, row[8:], label=f"{row['Indicator']} - {row['CE strat']}")
    
    # edit the plot
    plt.title('Development of "Vehicle Stocks for Gasoline, Diesel and BEVs" Over the Years for baseline SSP2 scenario')
    plt.xlabel('Year')
    plt.ylabel('Million vehicles')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()


# DEFINE DATAFRAMES FOR TYPE SPLIT FOR NEWLY REGISTERED VEHICLES
# difference is only between baseline and rcp scenario
# the customer behavior is taken into account here, calculating how quick a stock can shift towards more electric vehicles
type_split_baseline_LED = results[results['Indicator'].str.contains('type split of newly registered cars', case=False) 
                                  & results['Indicator'].str.contains('ICEG|ICED|BEV', case=False, regex=True) 
                                  & results['ClimPol scen'].str.contains('baseline', case=False) 
                                  & results['SocEc scen'].str.contains('LED', case=False) 
                                  & results['CE strat'].str.contains('with CE', case=False)]

type_split_rcp_LED = results[results['Indicator'].str.contains('type split of newly registered cars', case=False) 
                                  & results['Indicator'].str.contains('ICEG|ICED|BEV', case=False, regex=True) 
                                  & results['ClimPol scen'].str.contains('rcp', case=False) 
                                  & results['SocEc scen'].str.contains('LED', case=False) 
                                  & results['CE strat'].str.contains('with CE', case=False)]

def Type_split_new_cars_plots():
    # PLOT FIGURE BASELINE LED
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in type_split_baseline_LED.iterrows():
        plt.plot(years, row[8:], label=f"{row['Indicator']}")
    
    # edit the plot
    plt.title('Development of "Percentage Share for fuel types" Over the Years for baseline scenarios')
    plt.xlabel('Year')
    plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    plt.ylabel('Percentage share')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # PLOT THE RCP2.6 GRAPH    
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in type_split_rcp_LED.iterrows():
        plt.plot(years, row[8:], label=f"{row['Indicator']}")
    
    # edit the plot
    plt.title('Development of "Percentage Share for fuel types" Over the Years for RCP2.6 scenarios')
    plt.xlabel('Year')
    plt.gca().yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
    plt.ylabel('Percentage share')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()


# DEFINE VEHICLE STOCK RCP2.6 DATAFRAME
# for battery electric, gasoline, diesel
# showing the final stock composition and total stock for vehicle fleet in Freiburg
results_stock_baseline_LED = results[results['ClimPol scen'].str.contains('rcp', case=False) 
                                     & results['SocEc scen'].str.contains('LED', case=False) 
                                     & results['Indicator'].str.contains('In-use stock', case=False) 
                                     & results['Indicator'].str.contains('ICEG|ICED|BEV', case=False, regex=True)]
results_stock_baseline_SSP1 = results[results['ClimPol scen'].str.contains('rcp', case=False) 
                                      & results['SocEc scen'].str.contains('SSP1', case=False) 
                                      & results['Indicator'].str.contains('In-use stock', case=False) 
                                      & results['Indicator'].str.contains('ICEG|ICED|BEV', case=False, regex=True)]
results_stock_baseline_SSP2 = results[results['ClimPol scen'].str.contains('rcp', case=False) 
                                      & results['SocEc scen'].str.contains('SSP2', case=False) 
                                      & results['Indicator'].str.contains('In-use stock', case=False) 
                                      & results['Indicator'].str.contains('ICEG|ICED|BEV', case=False, regex=True)]

def Vehicle_stock_rcp_plots():
    # read in files
    # PLOT FIGURE RCP2.6 LED
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in results_stock_baseline_LED.iterrows():
        plt.plot(years, row[8:], label=f"{row['Indicator']} - {row['CE strat']}")
    
    # edit the plot
    plt.title('Development of "Vehicle Stocks for Gasoline, Diesel and BEVs" Over the Years for RCP2.6 LED scenario')
    plt.xlabel('Year')
    plt.ylabel('Million vehicles')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # PLOT FIGURE RCP2.6 SSP1
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in results_stock_baseline_SSP1.iterrows():
        plt.plot(years, row[8:], label=f"{row['Indicator']} - {row['CE strat']}")
    
    # edit the plot
    plt.title('Development of "Vehicle Stocks for Gasoline, Diesel and BEVs" Over the Years for RCP2.6 SSP1 scenario')
    plt.xlabel('Year')
    plt.ylabel('Million vehicles')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # PLOT FIGURE RCP2.6 SSP2
    plt.figure(figsize=(10, 6), facecolor='white')
    for i, row in results_stock_baseline_SSP2.iterrows():
        plt.plot(years, row[8:], label=f"{row['Indicator']} - {row['CE strat']}")
    
    # edit the plot
    plt.title('Development of "Vehicle Stocks for Gasoline, Diesel and BEVs" Over the Years for RCP2.6 SSP1 scenario')
    plt.xlabel('Year')
    plt.ylabel('Million vehicles')
    plt.legend(title='Scenario')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()


# The end.
