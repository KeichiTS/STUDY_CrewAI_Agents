import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

load_dotenv()


agente_mentor_godot = Agent(
    role='Mentor Godot Engine Para Iniciantes',
    goal='Ensinar os fundamentos de Godot Engine de forma clara',
    backstory=(
        'Você ensina iniciantes com linguagem acessível e exemplos simples.'
        'Foca em conceitos como variáveis, estruturas de controle e funções.'
    )
)

agente_especialista_gamedesign = Agent(
    role='Especialista em Gamedesign para jogos digitais',
    goal='Ajudar iniciantes sobre fundamentos de gamedesign',
    backstory=(
        'Você é um agente especializado em Gamedesign, conhece vários fundamentos teóricos para criar jogos divertidos'
    )
)

tarefa_guia_intro_godot = Task(
    description=(
        'Crie um guia introdutório sobre Godot Engine para iniciantes com explicações sobre'
        'GDScript, Functions, Nodes, Shaders'
    ),
    expected_output=(
        'Markdown com 5 seções explicando esses conceitos com exemplos e analogias simples.'
        'Em sua resposta evite marcadores como "```markdown" ou "```"'
        'Quero apenas o texto markdown com o conteúdo'
    ),
    agent=agente_mentor_godot,
    output_file='guias\guia_godot.md'
)

tarefa_guia_gamedesign = Task(
    description=(
        'Cria um guia introdutório sobre o fundamento de Gamedesign para jogos digitais'
    ),
    expected_output=(
        'Markdown com 5 seções explicando esses conceitos com exemplos e analogias simples.'
        'Em sua resposta evite marcadores como "```markdown" ou "```"'
        'Quero apenas o texto markdown com o conteúdo'
    ),
    agent=agente_especialista_gamedesign,
    output_file='guias\guia_gamedesign.md'
)

equipe = Crew(
    agents=[agente_mentor_godot, agente_especialista_gamedesign],
    tasks=[tarefa_guia_intro_godot,tarefa_guia_gamedesign],
    process= Process.sequential,
    verbose=True
)

resultado = equipe.kickoff()