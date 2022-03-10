import { resolve } from 'path'
import { readdirSync } from 'fs'
import handlebars from 'vite-plugin-handlebars'

let partials = resolve(__dirname, 'partials')
let project_files = readdirSync(__dirname)
    .filter((file) => file.startsWith("proj") && file.endsWith("html"))
let credits = [
    {
        url: "https://bigsky.software/",
        info: "HTMX and Hyperscript"
    },
    {
        url: "https://50projects50days.com/",
        info: "50 projects in 50 days"
    },
    {
        url: "https://fastapi.tiangolo.com/",
        info: "FastAPI"
    },
    {
        url: "https://domonic.readthedocs.io/",
        info: "Domonic"
    },
    {
        url: "https://glyphs.fyi/",
        info: "The Mightiest Icons"
    },
    {
        url: "https://grayshift.io/",
        info: "Grayshift CSS"
    },
    {
        url: "https://vitejs.dev/",
        info: "Vite Build Tool"
    },
    {
        url: "https://caddyserver.com/",
        info: "Caddy 2"
    },
]

export default {
    plugins: [
        handlebars({
            partialDirectory: partials,
            helpers: {
                project_title: (filename) => filename.replace(".html", "").replace("proj", "").split("_").join(" "),
            },
            context: {
                projects: project_files,
                credits,
            }
        }),
    ],
}
