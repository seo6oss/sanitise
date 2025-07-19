import graphviz
import click

@click.command()
@click.option('--output_file', default='workflow.png', help='The name of the output image file.')
def visualize_workflow(output_file):
    """Generates a workflow diagram."""
    dot = graphviz.Digraph(comment='iCloud Photo Manager Workflow')

    dot.node('A', 'User Input (Apple ID, 2FA)')
    dot.node('B', 'Download Photos')
    dot.node('C', 'Photos in DOWNLOAD_DIR')
    dot.node('D', 'Detect Duplicates (pHash)')
    dot.node('E', 'Duplicate List')
    dot.node('F', 'Filter Content (Expanded)')
    dot.node('G', 'Flagged Content List')
    dot.node('H', 'Generate Report (CSV)')
    dot.node('I', 'Confirm Deletion')
    dot.node('J', 'Local Deletion')
    dot.node('K', 'Manual iCloud Deletion')
    dot.node('L', 'Upload Garbage to iCloud')
    dot.node('M', 'Re-upload Cleaned Photos to iCloud')

    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('C', 'F')
    dot.edge('D', 'E')
    dot.edge('F', 'G')
    dot.edge('E', 'H')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    dot.edge('I', 'J')
    dot.edge('J', 'L')
    dot.edge('L', 'M')
    dot.edge('M', 'K')

    dot.render(output_file, view=False, format='png')
    click.echo(f"Workflow diagram saved to {output_file}")

if __name__ == '__main__':
    visualize_workflow()