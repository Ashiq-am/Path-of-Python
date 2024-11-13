from flask import Flask, render_template, request, redirect, url_for
from rich.console import Console
from rich.table import Table
import random

app = Flask(__name__)
console = Console()
