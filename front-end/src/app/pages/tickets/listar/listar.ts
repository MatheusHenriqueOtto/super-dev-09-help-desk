import { Component, inject, signal } from '@angular/core';
import { TicketService } from '../../../services/ticket.service';
import { TicketResposta } from '../../../models/tickets.model';
import { RouterLink } from '@angular/router';

@Component({
  imports: [RouterLink],
  selector: 'app-listar',
  styleUrl: './listar.scss',
  templateUrl: './listar.html',
})
export class Listar {
  ticketService = inject(TicketService);

  tickets =  signal<TicketResposta[]>([]);

  ngOnInit(){
    this.carregarTickets();
  }

  carregarTickets(){
    this.ticketService.listar().subscribe({
      next: (tickets) => this.tickets.set(tickets),
      error: (erro) => {
        console.error(erro)
        alert("Não foi possível carregar os tickets");
      }
    })
  }
}
