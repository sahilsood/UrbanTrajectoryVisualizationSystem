# UrbanTrajectoryVisualizationSystem
Coding Project: Improve an Urban Trajectory Visualization System


	Introduction 
In this project, the given prototype of a Visual analytics system for urban trajectory datasets has been modified to support data exploration and analytical reasoning with interactive visual interfaces. It allows users to interactively visualize and analyse the massive taxi trajectories over urban spaces. The interface offers data management capability and enable various visual queries through a web interface. The system should help the user to conduct visual analytics tasks through interactive visualization in an iterative, exploratory process. 
In this project, the given prototype of a Visual analytics system for urban trajectory datasets has been modified to support data exploration and analytical reasoning with interactive visual interfaces. It allows users to interactively visualize and analyse the massive taxi trajectories over urban spaces. The interface offers data management capability and enable various visual queries through a web interface. The system should help the user to conduct visual analytics tasks through interactive visualization in an iterative, exploratory process. 

	Implementation
The project has to be loaded from a local web server such as Web Server from Google. After the project is loaded, the index.html file will be displayed on the browser which contains a map interface of Taxi Trajectory data. User has to query the data by drawing a rectangle selection using the button on the bottom right of the screen.

	Query Result
After the query is made by drawing a rectangle, a call back function is called which will retrieve the data from the area that corresponds to the query region and displays taxi trip trajectories on the map.
 
	Tasks
The query result page will allow the user to view three different visualizations by accessing them through their respective links. Three level-2 tasks have been implemented in this prototype:

1.	Word Cloud
This visualization shows the most frequent street names by using an Interactive Word Cloud.
2.	Sankey Diagram
This Visualization show the top pick-up and drop-off street names with its relation by using an Interactive Sankey Diagram.
3.	Scatter-Matrix
This Visualization provides an interactive Scatter-Matrix to show the relationship between different attributes such as Av_Speed, Distance and Duration.
