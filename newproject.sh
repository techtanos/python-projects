#!/bin/bash
echo "Enter project name:"
read project_name
mkdir -p $project_name/src
mkdir -p $project_name/data
mkdir -p $project_name/scripts
mkdir -p $project_name/docs

echo "# $project_name" > $project_name/README.md
echo "Project '$project_name' created!"
echo "Folders: src, data, scripts, docs"
